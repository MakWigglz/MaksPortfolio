function Class (string1, string2){
  this.string1= string1;
  this.string2= string2;
}
Class.prototype.display = function(){
  return this.string1 + "and this " + this.string2;
  };
function Constructor(array){
  this.array=array;
}
String3.prototype.display = function(){
  var str="";
}
for (var i=0; i<this.array.length; i++)
    str += this.array[i].display() + " ";
        return str;
};
var myString3 = new myString3([
  new Class("myString1", "myString2"),
  new Class("myString4", "myString5"),
  new Class("myString6", "myString7")
  ]);
 alert(myString3.display() ); 






