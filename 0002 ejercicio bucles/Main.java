public class Main {

    public static void main (String[] args) {

        int numeroIf = 3;
        int numeroWhile = 1;
string estacion = "otoño";

        if (numeroIf > 0){
            System.out.println( "positivo");
        }else if (numeroIf < 0){
            System.out.println( "negativo");  
        }else {
            System.out.println( "cero");   
        }


        while (numeroWhile < 3) {
            System.out.println(numeroWhile); 
            numeroWhile ++;          
        }



        do {
            System.out.println(numeroWhile); 
            numeroWhile ++;   
        }while (numeroWhile <3);

        for (int numeroFor =0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);         
        }

    }

    switch (estacion){
        case "primavera":
             System.out.println("primavera"); 
             break;
        case "verano": 
            System.out.println("verano"); 
            break;
        case "otoño":
            System.out.println("otoño"); 
            break;
        case "invierno":
            System.out.println("invierno"); 
            break;
        case defalult:
            System.out.println("no es una estacion"); 

    }
 }



