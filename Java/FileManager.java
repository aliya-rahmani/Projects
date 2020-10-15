package singletonpractica;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.swing.JOptionPane;

public class FileManager {

    String testR = "C://config/null.txt";
    UserValidation u;

    public FileManager() {

        this.u = UserValidation.getIntance();

    }

    public void saveFile() {

        if (u.validateUser()) {

            String nameFile = JOptionPane.showInputDialog("Ingrese el nombre del archivo");
            String contentFile = JOptionPane.showInputDialog("Ingrese el contenido del archivo");

            String template = "C://config/%s.txt";
            String ruta = String.format(template, nameFile);

            try {

                File file = new File(ruta);
                // Si el archivo no existe es creado
                if (!file.exists()) {
                    file.createNewFile();
                }
                FileWriter fw = new FileWriter(file);
                BufferedWriter bw = new BufferedWriter(fw);
                bw.write(contentFile);
                bw.close();

                System.out.println("Archivo creado con exito");

            } catch (Exception e) {
                e.printStackTrace();
            }

        } else {
            System.err.println("Error");
        }

    }

    public void readFile() {

        if (u.validateUser()) {

            String nameFile = JOptionPane.showInputDialog("Ingrese el nombre del archivo a leer");

            File archivo = null;
            FileReader fr = null;
            BufferedReader br = null;

            String template = "C://config/%s.txt";
            String ruta = String.format(template, nameFile);

            try {
                // Apertura del fichero y creacion de BufferedReader para poder
                // hacer una lectura comoda (disponer del metodo readLine()).
                archivo = new File(ruta);
                fr = new FileReader(archivo);
                br = new BufferedReader(fr);

                // Lectura del fichero
                String linea;
                while ((linea = br.readLine()) != null) {
                    System.out.println(linea);
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                // En el finally cerramos el fichero, para asegurarnos
                // que se cierra tanto si todo va bien como si salta 
                // una excepcion.
                try {
                    if (null != fr) {
                        fr.close();
                    }
                } catch (Exception e2) {
                    e2.printStackTrace();
                }

            }
        } else {
            System.err.println("Error");
        }

    }

    public void changeDataUser() {

        if (u.validateUser()) {

            delUserFile();
            
            String user = JOptionPane.showInputDialog("Ingrese el nuevo nombre de usuario");
            String pass = JOptionPane.showInputDialog("Ingrese la nueva contrasenha");

            String ruta = "C://config/user.txt";

            try {

                File file = new File(ruta);
                // Si el archivo no existe es creado
                if (!file.exists()) {
                    file.createNewFile();
                }
                FileWriter fw = new FileWriter(file);
                BufferedWriter bw = new BufferedWriter(fw);
                bw.write(user);
                bw.write("\n");
                bw.write(pass);
                bw.close();

                System.out.println("Archivo creado con exito");

            } catch (Exception e) {
                e.printStackTrace();
            }

        } else {
            System.err.println("Error");
        }

    }

    public static void delUserFile() {

        File archivo = null;
        String ruta = "C://config/user.txt";

        try {
            /*Si existe el fichero*/
            archivo = new File(ruta);
            if (archivo.exists()) {
                /*Borra el fichero*/
                archivo.delete();
            }
        } catch (Exception ex) {
            /*Captura un posible error y le imprime en pantalla*/
            System.out.println(ex.getMessage());
        }
    }

}
