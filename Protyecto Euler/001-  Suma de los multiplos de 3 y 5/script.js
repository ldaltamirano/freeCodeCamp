function multiplesOf3and5(number) {
    let suma = 0;
    let multiplo = 1;
    do {
        if (multiplo % 3 == 0 || multiplo % 5 == 0) {
            suma += multiplo;
        }
        multiplo++;
    } while (multiplo < number);

    return suma;
}

multiplesOf3and5(1000);