function telephoneCheck(str) {
    let regexp = "^1? ?([(]{0}[0-9]{3}[)]{0}|[(]{1}[0-9]{3}[)]{1}) ?-?[0-9]{3} ?-?[0-9]{4}$"

    const regexp1 = new RegExp(regexp);
    let correct = regexp1.test(str);
    if(correct) {
        return true;
    }
    return false;
}
  
telephoneCheck("1 (555) 555-5555");