import * as THREE from '../build/three.module.js';
import {OrbitControls} from "../examples/jsm/controls/OrbitControls.js";
import {RectAreaLightUniformsLib} from "../examples/jsm/lights/RectAreaLightUniformsLib.js";
import {RectAreaLightHelper} from "../examples/jsm/helpers/RectAreaLightHelper.js";

class App {
    constructor() {
        const divContainer = document.querySelector("#webgl-container ");
        this._divContainer = divContainer;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setPixelRatio(window.devicePixelRatio);
        divContainer.appendChild(renderer.domElement);
        this._renderer = renderer;

        const scene = new  THREE.Scene();
        this._scene = scene;

        this._setupCamera();
        this._setupLight();
        this._setupModel();
        this._setupControls();

        window.onresize = this.resize.bind(this);
        this.resize();

        requestAnimationFrame(this.render.bind(this));
    }

    _setupControls() {
        new OrbitControls(this._camera, this._divContainer);
    }

    _setupCamera() {
        const width = this._divContainer.clientWidth;
        const height = this._divContainer.clientHight;
        const camera = new THREE.PerspectiveCamera(
            75,
            width / height,
            0.1,
            100
        );
        //camera.position.z = 5
        camera.position.set(7, 7, 0);
        camera.lookAt(0, 0, 0);
        this._camera = camera;
    }

    _setupLight() {
        /*
        // const light = new THREE.AmbientLight(0xff0000, 5);

        //const light = new THREE.HemisphereLight("#b0d8f5", "#dd7a1c", 1)

        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(0, 5, 0);
        light.target.position.set(0, 0, 0);
        this._scene.add(light.target);

        // 광원 시각화
        const helper = new THREE.DirectionalLightHelper(light);
        this._scene.add(helper);
        this._lightHelper = helper;
        
        this._scene.add(light);
        this._light = light;
        */

        /*
        // point light
        const light = new THREE.PointLight(0xffffff, 2);
        light.position.set(0, 5, 0);

        light.distance = 0;
        
        const helper = new THREE.PointLightHelper(light);
        this._scene.add(helper);

        this._scene.add(light);
        this._light = light;
        */

        /*
        // Spot light
        const light = new THREE.SpotLight(0xffffff, 1);
        light.position.set(0, 5, 0);
        light.target.position.set(0, 0, 0);
        light.angle = THREE.Math.degToRad(30);
        light.penumbra = 1;
        this._scene.add(light.target);

        const helper = new THREE.SpotLightHelper(light);
        this._scene.add(helper);
        this._lightHelper = helper;

        this._scene.add(light);
        this._light = light;
        */

        // 형광등 느낌.
        RectAreaLightUniformsLib.init();
        
        const light = new THREE.RectAreaLight(0xffffff, 10, 6, 1);
        light.position.set(0, 5, 0);
        light.rotation.x = THREE.Math.degToRad(-90);

        const helper = new RectAreaLightHelper(light);
        this._scene.add(helper);

        this._scene.add(light);
        this._light = light;
    }

    _setupModel() {
        // ground
        const groundGeometry = new THREE.PlaneGeometry(10, 10);
        const groundMatrial = new THREE.MeshStandardMaterial({
            color: "#2c3e50",
            roughness: 0.5,
            metalness: 0.5,
            side: THREE.DoubleSide
        });

        const ground = new THREE.Mesh(groundGeometry, groundMatrial);
        ground.rotation.x = THREE.Math.degToRad(-90);
        this._scene.add(ground);

        const bigSphereGeometry = new THREE.SphereGeometry(1.5, 64, 64, 0, Math.PI);
        const bigSphereMatrial = new THREE.MeshStandardMaterial({
            color: "#ffffff",
            roughness: 0.1,
            metalness: 0.2,
        });
        const bigSphere = new THREE.Mesh(bigSphereGeometry, bigSphereMatrial);
        bigSphere.rotation.x = THREE.Math.degToRad(-90);
        this._scene.add(bigSphere);

        const torusGeometry = new THREE.TorusGeometry(0.4, 0.1, 32, 32);
        const torusMatrial = new THREE.MeshStandardMaterial({
            color: "#9b59b6",
            roughness: 0.5,
            metalness: 0.9,
        });

        for(let i=0 ; i<8; i++) {
            const torusPivot = new THREE.Object3D();
            const torus = new THREE.Mesh(torusGeometry, torusMatrial);
            torusPivot.rotation.y = THREE.Math.degToRad(45 * i)
            torus.position.set(3, 0.5, 0);
            torusPivot.add(torus);
            this._scene.add(torusPivot);
        }

        const smallSphereGeometry = new THREE.SphereGeometry(0.3, 32, 32);
        const smallSphereMatrial = new THREE.MeshStandardMaterial({
            color: "#e74c3c",
            roughness: 0.2,
            metalness: 0.5,
        });
        const smallSpherePivot = new THREE.Object3D();
        const smallSphere = new THREE.Mesh(smallSphereGeometry, smallSphereMatrial);
        smallSpherePivot.add(smallSphere);
        smallSpherePivot.name = "smallSpherePivot";
        smallSphere.position.set(3, 0.5, 0);
        this._scene.add(smallSpherePivot);
    }

    resize() {
        const width = this._divContainer.clientWidth;
        const height = this._divContainer.clientHeight;

        this._camera.aspect = width / height;
        this._camera.updateProjectionMatrix();

        this._renderer.setSize(width, height);
    }

    render(time) {
        this._renderer.render(this._scene, this._camera);
        this.update(time);
        requestAnimationFrame(this.render.bind(this));
    }

    update(time) {
        time *= 0.001;

        const smallSpherePivot = this._scene.getObjectByName("smallSpherePivot");
        if(smallSpherePivot) {
            smallSpherePivot.rotation.y = THREE.Math.degToRad(time * 50);

            /*
            if(this._light.target) {
                const smallSphere = smallSpherePivot.children[0];
                smallSphere.getWorldPosition(this._light.target.position);

                if(this._lightHelper) {
                    this._lightHelper.update();
                }
            }
            */
            
            /*
            // point light
            if(this._light) {
                const smallSphere = smallSpherePivot.children[0];
                smallSphere.getWorldPosition(this._light.position);

                if(this._lightHelper) {
                    this._lightHelper.update();
                }
            }
            */

            if(this._light.target) {
                const smallSphere = smallSpherePivot.children[0];
                smallSphere.getWorldPosition(this._light.target.position);

                if(this._lightHelper) {
                    this._lightHelper.update();
                }
            }
        }
    }
}

window.onload = function() {
    new App();
}