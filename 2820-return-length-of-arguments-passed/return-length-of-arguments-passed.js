/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let count = 0
  console.log(args,...args)
  for(let i = 0;i<args.length;i++){
    count++
  }  
  return count


};

/**
 * argumentsLength(1, 2, 3); // 3
 */