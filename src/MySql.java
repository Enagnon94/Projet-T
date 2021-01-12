import java.sql.Connection;
import java.sql.DriverManager;

public class MySql {

    public static void main(String[] args) {

        String connectionUrl = "jdbc:sqlserver://localhost:3306;databaseName=IoT;user=Enagnon;password=bdd";

        try {
            // Load SQL Server JDBC driver and establish connection.
            System.out.print("Connecting to SQL Server ... ");
            try (Connection connection = DriverManager.getConnection(connectionUrl)) {
                System.out.println("Done.");
            }
        } catch (Exception e) {
            System.out.println();
            e.printStackTrace();
        }
    }
}