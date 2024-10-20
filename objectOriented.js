function Class (string1, string2){
  this.string1= string1;
  this.string2= string2;
}
Class.prototype.display = function(){
  return this.string1 + "and this " + this.string2;
  };
