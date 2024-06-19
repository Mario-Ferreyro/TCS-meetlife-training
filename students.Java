import java.util.Random;

public class Student {
    private int studentId;
    private String firstName;
    private String middleName;
    private String lastName;
    private String dob; // Date of Birth

    public Student(String firstName, String middleName, String lastName, String dob) {
        this.studentId = new Random().nextInt(10000); // Random number as Student ID
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.dob = dob;
    }

    public String getFullName() {
        return firstName + " " + middleName + " " + lastName;
    }

    public void displayStudentDetails() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Full Name: " + getFullName());
        System.out.println("Date of Birth: " + dob);
    }

    public static void main(String[] args) {
        Student sdnt1 = new Student("Mario", "Perez", "Ferreyro", "07/11/1995");
        Student sdnt2 = new Student("Leroy", "TPK", "Jenklings", "11/07/1998");
        Student sdnt3 = new Student("Marcos", "Rovinn", "Rossi", "03/03/2001");

        sdnt1.displayStudentDetails();
        sdnt2.displayStudentDetails();
        sdnt3.displayStudentDetails();
    }
}
