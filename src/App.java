
public class App {
    public static void main(String[] args) {
       
       System.out.println("Coucou");
       Feu feu = new Feu(2,2,0,0);
       feu.etat();
       feu.allumer();
       System.out.println(feu.getCoord());
       
       
    }
}
