a()
b()
function a(){
  console.log("a")
}
function b(){
  console.log("b")
}

let arr = [1,2,3,4,5]
let newarr =arr.reverse().filter(remove)
function remove(arr){
 return arr !=2 && arr != 5 
}
console.log(newarr)
