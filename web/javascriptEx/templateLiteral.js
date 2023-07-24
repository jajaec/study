// 자바스크립트 실행 방법 
// node.js 설치되어야 한다.
// 실행: Ctrl + Alt + N
// 한글깨짐 발생시 인코딩 조절한다.

console.log('\n// 1. 템플릿 리터럴(Template literal)');
const teslaModel3 = {
    carName: 'sexy',
    price: 37990,
    madeIn: ['중국', '미국'],
    release: 2019
};
return;

const { carName, price, madeIn } = teslaModel3;
myCar = `${carName}는 ${price}에 구매했고 ${madeIn[0]}에서 생산되었다.`;

console.log(myCar);

console.log('\n// 2. 비구조화 할당(Destructuring)');
const car = {
    carName: '테슬라',
    fuel: '전기배터리',
    drivingMethod: '자율주행 레벨3',
    maximumSpeed: 255,
    zeroBack: 5.6,
}

function driving2({ carName, zeroBack, maximumSpeed }) {
    return `${carName}는 ${zeroBack}만에 ${maximumSpeed} kph로 달린다.`;
}

console.log(driving2(car));

function driving3(car) {
    const { carName, zeroBack, maximumSpeed } = car;
    return `${carName}는 ${zeroBack}만에 ${maximumSpeed} kph로 달린다.`;
}

console.log(driving3(car));

console.log('\n// 3. spread 연산자 (Spread syntax)');
const ElonReeveMusk = { name: 'Elon Reeve Musk' };
const companyValue = { tesla: 2400, spaceX: 100, openAI: 80 };

const ElonReeveMusk_Value2_in_2020 = { ...ElonReeveMusk, ...companyValue };
const ElonReeveMusk_Value2_in_2021 = { ...ElonReeveMusk, tesla: 4800 };
console.log(ElonReeveMusk_Value2_in_2020);
console.log(ElonReeveMusk_Value2_in_2021);


let FAANG = ['FaceBook', 'Amazon'];
FAANG = [...FAANG, 'Apple', 'Netflix', 'Google'];
console.log(FAANG);

let FAANG2 = ['FaceBook', 'Amazon'];
FAANG2 = ['Apple', 'Netflix', 'Google', ...FAANG2];
console.log(FAANG2);

let FAANG3 = ['FaceBook', 'Amazon'];
FAANG3 = ['Apple', ...FAANG3, 'Netflix', 'Google'];
console.log(FAANG3);

console.log('\n// 4. 반복하기(Loops)');
const carts = [
    { name: 'tesla', price: 2800 },
    { name: 'apple', price: 500 },
    { name: 'google', price: 1000 },
    { name: 'facebook', price: 2000 },
    { name: 'amazon', price: 1500 },
];

const total2 = carts.reduce((acc, cur) => acc + cur.price, 0);
const withFee2 = carts.map((cart) => cart.price + 1.05);
const highPrices = carts.filter((cart) => cart.price > 1500);

console.log(total2);
console.log(withFee2);
console.log(highPrices);

console.log('\n// 5. async/await');
const random = () => {
    return Promise.resolve(Math.random());
}

const sumNumber2 = async () => {
    const first = await random();
    const second = await random();
    const third = await random();

    console.log(`Result(${first} + ${second} + ${third}): ${first + second + third}`);
    return first + second + third;
};
sumNumber2();

/*
console.log('\n// 6. 함수 생성 시점과 호이스팅');
//함수 참조중
console.dir(add);
console.dir(sub);

//함수 호출중
console.log(add(2,5));
console.log(sub(2,5));  // 표현식은 런타임 이후 이므로 실행 시 오류 발생 함.

//함수 선언문은 런타임 이전에 자바스크립트 엔진에 의하여 실행됨.
function add(x,y) {
  return x + y;
}

//함수 표현식은 런타임 이후
var sub = function(x,y) {
  return x - y;
}

console.log(sub(2,5));  // 표현식 선언이후 사용해야 함.
*/