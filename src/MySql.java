
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MySql {
        // Connect to your database.
        // Replace server name, username, and password with your credentials
        public static void main(String[] args) {
            String connectionUrl =
                    "jdbc:sqlserver://localhost:3306;"
                            + "database=IoT;"
                            + "user=Enagnon;"
                            + "password=bdd;"
                            + "encrypt=true;"
                            + "trustServerCertificate=false;"
                            + "loginTimeout=30;";
    
            try (Connection connection = DriverManager.getConnection(connectionUrl);) {
                System.out.println("Connection !!!");
                // Code here.
            }
            // Handle any errors that may have occurred.
            catch (SQLException e) {
                System.out.println("Error");
                e.printStackTrace();                
            }
        }
    }
    