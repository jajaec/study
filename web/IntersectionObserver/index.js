const squares = document.querySelectorAll("div");

const observer = new IntersectionObserver(
    (squares) => {
        squares.forEach((square) => {
            if (square.isIntersecting) {    // 타겟이 화면 안으로 들어오면
                square.target.classList.add("visible");
            } else {    // 타겟이 화면밖으로 사라지면
                square.target.classList.remove("visible");
            }
        });
    },
    {
        threshold: 0.5  // 타켓이 50%이상 보이면
    }
);

squares.forEach((square) => observer.observe(square));