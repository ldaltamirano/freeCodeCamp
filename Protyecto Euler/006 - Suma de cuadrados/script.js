function sumSquareDifference(n) {

    let sumCuadrados = 0
    let sumAlCuadrado = 0;

    for (let index = 1; index <= n; index++) {

        sumCuadrados += Math.pow(index,2);
        sumAlCuadrado += index;
    }

    sumAlCuadrado = math.pow(sumAlCuadrado,2);

    return sumAlCuadrado - sumAlCuadrado; 

  }
  
  sumSquareDifference(100);