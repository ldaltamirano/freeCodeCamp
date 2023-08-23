function specialPythagoreanTriplet(n) {
    var a;
    var c;

    for (var b = 1; b < n; b += 1) {
        a = (Math.pow(n,2)/2 - n * b) / (n - b);

        if (Math.floor(a) === a) {
            c = n - a - b;

            break;
        }
    }

    return a * b * c;
}

console.log(specialPythagoreanTriplet(24));


