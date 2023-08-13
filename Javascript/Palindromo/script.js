function palindrome(str) {
    let word = "";
    str = str.toLowerCase();
    for (let index = 0; index < str.length; index++) {
        let correct = str[index].search("[a-zA-Z0-9]");
        if(correct >= 0) {
            word += str[index];
        }
    }

    for (let index = 0; index < word.length; index++) {
        if(word[index] != word[word.length - index -1]) {
            return false;
        }
    }

    return true;
}
  
palindrome("1 eye for of 1 eye.");