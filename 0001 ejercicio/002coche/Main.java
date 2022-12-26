class Main {
    public static void main (String[] args) {
        //creamos un coche, que tendra por defecto 2 puertas
        Coche micoche = new Coche();

        //añadimos una puerta al coche
        micoche.incrementaPuertas();

        //mostramos el numero de puertas
        System.out.println( micoche.npuertas);
    }
}

class Coche {
    //creo un coche con como mínimo 2 puertas
    public int npuertas=2;

    public void incrementaPuertas(){
        this.npuertas++;
    }
}



