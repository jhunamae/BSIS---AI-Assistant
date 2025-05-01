// MATRIX ANIMATION
const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

const letters = "01".split("");
const fontSize = 16;
const columns = canvas.width / fontSize;
const drops = [];

for (let x = 0; x < columns; x++) drops[x] = 1;

function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#00ff99";
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
        const text = letters[Math.floor(Math.random() * letters.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }

        drops[i]++;
    }
}

setInterval(draw, 10);

// RESPONSE TYPING EFFECT
if (document.getElementById("response-data")) {
    const response = JSON.parse(document.getElementById("response-data").textContent);
    const answerBox = document.getElementById("answer-box");

    const lines = response.split('\n');
    let lineIndex = 0;

    function typeLine(line, callback) {
        let i = 0;
        let typedLine = '';

        const p = document.createElement('p');
        p.style.marginLeft = line.trim().toLowerCase().startsWith("step") ? '20px' : '0';
        answerBox.appendChild(p);

        function typeChar() {
            if (i < line.length) {
                typedLine += line.charAt(i);
                p.textContent = typedLine;
                p.scrollIntoView({ behavior: "smooth", block: "end" });
                i++;
                setTimeout(typeChar, 10);
            } else {
                callback();
            }
        }

        typeChar();
    }

    function typeAllLines() {
        if (lineIndex < lines.length) {
            typeLine(lines[lineIndex], () => {
                lineIndex++;
                typeAllLines();
            });
        }
    }

    typeAllLines();
}


function submitSuggestion(text) {
    const input = document.getElementById("question-input");
    const form = document.getElementById("question-form");

    input.value = text;
    form.submit();
}