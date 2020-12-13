import java.lang.System.Logger;
import java.lang.reflect.Method;
import java.security.KeyStore.Entry.Attribute;

public class Feu {
        private  int X, Y;
        private int intensite;
        private int rayon;

        public Feu(int x,int y, int intensite, int rayon) {
           this.X = x;
           this.Y = y;
           this.intensite = intensite;
           this.rayon = rayon;
           
           System.out.format("Génération d'un élément Feu aux coordonnees : %d %d%n",X,Y);
           
        }
        public int[] etat(){
                int[] etat = {this.X,this.Y,this.intensite,this.rayon};
                System.out.format("X : %d Y : %d Intensité : %d Rayon : %d%n",etat[0],etat[1],etat[2],etat[3]);
                return etat ;


        }
        public void allumer(){
                if (this.intensite == 1){System.out.println("Feu deja allumé%n")}
                else{this.intensite = 1;}
        }

        public void eteindre(){
                this.intensite = 1;
        }


    }
    