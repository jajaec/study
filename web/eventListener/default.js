const outer = document.querySelector('.outer');
const middle = document.querySelector('.middle');
const inner1 = document.querySelector('.inner1');
const inner2 = document.querySelector('.inner2');

const capture = {
    capture: true
};
const noneCapture = {
    capture: false
};
const once = {
    once: true
};
const noneOnce = {
    once: false
};
const passive = {
    passive: true
};
const nonePassive = {
    passive: false
};

// outer.addEventListener('click', onceHandler);
// outer.addEventListener('click', noneOnceHandler);
// middle.addEventListener('click', captureHandler);
// middle.addEventListener('click', noneCaptureHandler);
// inner1.addEventListener('click', passiveHandler);
// inner2.addEventListener('click', nonePassiveHandler);

outer.addEventListener('click', onceHandler, once);
outer.addEventListener('click', noneOnceHandler, noneOnce);
middle.addEventListener('click', captureHandler, capture);
middle.addEventListener('click', noneCaptureHandler, noneCapture);
inner1.addEventListener('click', passiveHandler, passive);
inner2.addEventListener('click', nonePassiveHandler, nonePassive);

function onceHandler(event) {
    console.log(event);
    alert('바깥, 일회용');
}
function noneOnceHandler(event) {
    console.log(event);
    alert('바깥, 다회용, 기본 값');
}
function captureHandler(event) {
    console.log(event);
    //event.stopImmediatePropagation();
    alert('중간, 캡처');
}
function noneCaptureHandler(event) {
    console.log(event);
    alert('중간, 비 캡처, 기본 값');
}
function passiveHandler(event) {
    console.log(event);
    // 패시브 수신기 내에서는 preventDefault 사용 불가
    event.preventDefault();
    alert('내부 1, 패시브, 새 페이지 열림');
}
function nonePassiveHandler(event) {
    console.log(event);
    event.preventDefault();
    //event.stopPropagation();
    alert('내부 2, 비 패시브, 기본 값, 새 페이지 열림');
}
