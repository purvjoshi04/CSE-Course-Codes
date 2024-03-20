const student = {
    name: "John",
    sclass: "VI",
    rollno: 12,
    get classRoll() {
      if (this.sclass === "VI") {
        return this.rollno;
      } else if (this.sclass === "V") {
        return 13;
      } else {
        return null; 
      }
    },
    set classRoll(newRoll) {
      if (this.sclass === "VI") {
        this.rollno = newRoll;
      } else {
        console.log("Cannot update rollno for sclass other than VI");
      }
    }
  };
  console.log(student);
  console.log("Class Roll:", student.classRoll);
  student.classRoll = 15;
  console.log(student);
  