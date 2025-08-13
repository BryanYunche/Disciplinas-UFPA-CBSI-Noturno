var canvas = document.getElementById("myCanvas"); // Obtém o elemento canvas pelo ID
var ctx = canvas.getContext("2d"); // Obtém o contexto 2D do canvas para desenhar nele

var cellWidth = 20; // Define a largura de cada célula da grade de pixels
var cellHeight = 20; // Define a altura de cada célula da grade de pixels

function desenhar() {
    var pontosInput = document.getElementById("pontos"); // Obtém o valor do campo de entrada de pontos
    var pontos = JSON.parse(pontosInput.value); // Converte a string JSON em uma lista de pontos

    // Limpa o canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Desenha a grade de pixels
    for (var x = -canvas.width / 2; x < canvas.width / 2; x += cellWidth) {
        for (var y = -canvas.height / 2; y < canvas.height / 2; y += cellHeight) {
            ctx.fillStyle = "white"; // Define a cor de preenchimento como branco
            ctx.fillRect(canvas.width / 2 + x, canvas.height / 2 + y, cellWidth, cellHeight); // Desenha um retângulo branco preenchido para cada célula da grade
            ctx.strokeStyle = "black"; // Define a cor do contorno como preto
            ctx.strokeRect(canvas.width / 2 + x, canvas.height / 2 + y, cellWidth, cellHeight); // Desenha o contorno preto para cada célula da grade
        }
    }

    // Desenha pontos na lista
    for (var i = 0; i < pontos.length; i++) {
        var ponto = pontos[i];
        ctx.fillStyle = "black"; // Define a cor de preenchimento como preto
        ctx.fillRect(canvas.width / 2 + ponto[0] * cellWidth + cellWidth / 2, canvas.height / 2 - ponto[1] * cellHeight - cellHeight / 2, cellWidth, cellHeight); // Desenha um retângulo preto preenchido para cada ponto na lista
    }
}

