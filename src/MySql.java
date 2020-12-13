import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class MySql {
        private static final Connection conn;
        public MySql() throws SQLException{

        try{    
                
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/IoT","Enagnon","bdd");  
                                                  //here sonoo is database name, root is username and password  
              //  Statement stmt = conn.createStatement();  
             //   ResultSet rs = stmt.executeQuery("select * from emp");  
             //   while(rs.next()) {
                //System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getString(3));  }
                conn.close();  
                }catch (Exception e){ System.out.println(e);}  

        }         
        
}

