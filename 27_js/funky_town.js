var fact = function(n){
   if (n == 1){
      return 1;
   }
   return n*fact(n-1);
};

var fib = function(n){
    if (n == 1){
        return 1;
    }
    if (n == 2){
        return 1;
    }
    return fib(n - 1) + fib(n - 2)
};

var gcd = function(a, b){
    if (a == 0){
        return b;
    }
    return gcd(b % a, a)
};
