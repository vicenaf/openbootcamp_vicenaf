
/*
Crea una clase Persona con las siguientes variables:

La edad
El nombre
El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase
tendrá la variable credito solo para esa clase.

Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad,
el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y
con una variable salario que solo tenga la clase Trabajador.
 */


public class Main {

    public static void main (String[] args) {

        Cliente yomismocliente = new Cliente();

        yomismocliente.setEdad(999);
        yomismocliente.setNombre("Miquelangelo");
        yomismocliente.setTelefono(555012345);
        yomismocliente.setCredito(999999999);

        System.out.println(yomismocliente.getNombre());
        System.out.println(yomismocliente.getEdad());
        System.out.println(yomismocliente.getTelefono());
        System.out.println(yomismocliente.getCredito());


        Trabajador yomismotrabajador = new Trabajador();

        yomismotrabajador.setEdad(888);
        yomismotrabajador.setNombre("Donatello");
        yomismotrabajador.setTelefono(321321321);
        yomismotrabajador.setsalario(888888);

        System.out.println(yomismotrabajador.getNombre());
        System.out.println(yomismotrabajador.getEdad());
        System.out.println(yomismotrabajador.getTelefono());
        System.out.println(yomismotrabajador.getsalario());

    }
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getTelefono() {
        return telefono;
    }
    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

}


/*
Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad,
el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
*/

class Cliente extends Persona {

    public int credito;
    public int getCredito() {
        return credito;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }


}


/*
Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una
variable salario que solo tenga la clase Trabajador.
 */
class Trabajador extends Persona {

    public int salario;

    public int getsalario() {
        return salario;
    }

    public void setsalario(int salario) {
        this.salario = salario;
    }

}