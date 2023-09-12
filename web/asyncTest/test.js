//import * as util from './util.js';


// document.getElementById("test7").onclick = function () {
//     alert("Hello World");
// };
document.getElementById("test7").addEventListener('click', test07);

function test01() {
    console.log("모두에게 일을 시켜보자!")
    setTimeout(() => {
        console.log("A: 일을 마쳤습니다.")
    }, 1000);
    setTimeout(() => {
        console.log("B: 일을 마쳤습니다.")
    }, 1000);
    setTimeout(() => {
        console.log("C: 일을 마쳤습니다.")
    }, 1000);
    console.log("일은 전부 시켜놓았다!")
}

function test02() {
    console.log("모두에게 일을 시켜보자! (각 팀원은 1~2초의 소요시간이다.)");

    let aFinished = false;
    let bFinished = false;
    let cFinished = false;

    setTimeout(
        () => {
            console.log("A: 일을 마쳤습니다!");
            aFinished = true;
            if (aFinished && bFinished && cFinished) {
                console.log("일을 다 마쳤으니 이제 요리를 시작하자!");
            }
        },
        Math.random() * 1000 + 1000,
    );

    setTimeout(
        () => {
            console.log("B: 일을 마쳤습니다!");
            bFinished = true;
            if (aFinished && bFinished && cFinished) {
                console.log("일을 다 마쳤으니 이제 요리를 시작하자!");
            }
        },
        Math.random() * 1000 + 1000,
    );

    setTimeout(
        () => {
            console.log("C: 일을 마쳤습니다!");
            cFinished = true;
            if (aFinished && bFinished && cFinished) {
                console.log("일을 다 마쳤으니 이제 요리를 시작하자!");
            }
        },
        Math.random() * 1000 + 1000,
    );

    console.log("일은 전부 시켜놓았다!");
}

function startAsync1(age) {
    return new Promise((resolve, reject) => {
        if (age > 20) resolve(`${age} success`);
        else reject(new Error(`${age} is not over 20`));
    });
}

async function startAsync(age) {
    if (age > 20) return `${age} success`;
    else throw new Error(`${age} is not over 20`);
}

function test03() {
    const promise1 = startAsync(25);
    promise1
        .then((value) => {
            console.log(value);
        })
        .catch((error) => {
            console.error(error);
        });

    const promise2 = startAsync(15);
    promise2
        .then((value) => {
            console.log(value);
        })
        .catch((error) => {
            console.error(error);
        });
}

function setTimeoutPromise(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(), ms);
    });
}

async function fetchAge(id) {
    await setTimeoutPromise(1000);
    console.log(`${id} 사원 데이터 받아오기 완료!`);
    return parseInt(Math.random() * 20, 10) + 25;
}

async function test04() {
    let ages = [];
    for (let i = 0; i < 10; i++) {
        let age = await fetchAge(i);
        ages.push(age);
    }

    console.log(
        `평균 나이는? => ${ages.reduce((prev, current) => prev + current, 0) / ages.length
        }`
    );
}

async function test05() {
    const ids = Array.from({ length: 10 }).map((_, index) => index);
    const promises = ids.map(fetchAge);
    const ages = await Promise.all(promises);

    console.log(
        `평균 나이는? => ${ages.reduce((prev, current) => prev + current, 0) / ages.length
        }`
    );
}

async function test06() {
    fetch("http://localhost/google/get_package_list").then((response) =>
        console.log(response)
    );
}


async function prepareOneFish() {
    let start = new Date().getTime();
    while (new Date().getTime() < start + 1000) {
        // preparing fish
    }
    return "finished";
}

function test07() {
    alert("test");
    console.log(util.add([1, 2, 3]));

    // console.log("Start!");
    // prepareOneFish().then(console.log);
    // prepareOneFish().then(console.log);
    // prepareOneFish().then(console.log);
    // console.log("Finish!");
}