

  function nthPrime(nth) {
    var arr = [2];
    var isPrime = true;

    for(var i = 3; arr.length < nth; i++) {
        isPrime = true;
        for(var j = 2; j < i; j++) {
            if(i % j === 0) {
                isPrime = false;
                break;

            }
        }
        if(isPrime === true) {
            arr.push(i);
        }
    }
    return arr[arr.length-1];
}

nthPrime(4);

