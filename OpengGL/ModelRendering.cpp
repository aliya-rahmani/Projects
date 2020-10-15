#include<GL/gl.h>
#include<GL/glut.h>
#include<math.h>
#include<vector>
#include<cstdio>
#include<string.h>



bool loadOBJ(const char * path,std::vector < std::vector<float>> & out_vertices,std::vector < std::vector<int> > & out_faces)
{
    FILE * file = fopen(path, "r");
    if( file == NULL ){
        printf("Error in opening the file !\n");
        return false;
    }
    while( 1 ){

        char lineHeader[128];
        // read the first word of the line
        int res = fscanf(file, "%s", lineHeader);
        if (res == EOF)
            break; // EOF = End Of File. Quit the loop.

        if ( strcmp( lineHeader, "v" ) == 0 ){
            std::vector<float> vertex(3);
            fscanf(file, "%f %f %f\n", &vertex[0], &vertex[1], &vertex[2] );
            out_vertices.push_back(vertex);
        }
        else if ( strcmp( lineHeader, "f" ) == 0 ){
            std::vector<int> vertexIndex(3);
            fscanf(file, "%d %d %d\n", &vertexIndex[0], &vertexIndex[1],&vertexIndex[2] );
            
            out_faces.push_back(vertexIndex);
        }
    }
    return true;
}



void normalize(float v[3]) {    
   GLfloat d = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]); 
   if (d == 0.0) {
      return;
   }
   v[0] /= d; v[1] /= d; v[2] /= d; 
}

void normcrossprod(float v1[3], float v2[3], float out[3]) 
{ 

   out[0] = v1[1]*v2[2] - v1[2]*v2[1]; 
   out[1] = v1[2]*v2[0] - v1[0]*v2[2]; 
   out[2] = v1[0]*v2[1] - v1[1]*v2[0]; 
   normalize(out); 
}

void display(){
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    std::vector<std::vector<float>> vertices;
    std::vector<std::vector<int>> faces;
    bool loadSuccess = loadOBJ("lowpolybunny.obj",vertices,faces);
    if(!loadSuccess)
        return;

    int num_of_vertices = vertices.size();

    int num_of_faces = faces.size();
    


    for (int i = 0; i < num_of_faces; i++) {    

        glBegin(GL_TRIANGLES);
        GLfloat d1[3], d2[3], norm[3];    
        for (int j = 0; j < 3; j++) {    
            d1[j] = vertices[faces[i][0]-1][j] - vertices[faces[i][1]-1][j];    
            d2[j] = vertices[faces[i][1]-1][j] - vertices[faces[i][2]-1][j];    
        }
        normcrossprod(d1, d2, norm); 
        glNormal3fv(norm);
        glVertex3fv(&vertices[faces[i][0]-1][0]); 
        glVertex3fv(&vertices[faces[i][1]-1][0]); 
        glVertex3fv(&vertices[faces[i][2]-1][0]);
        glEnd(); 
    }

    glutSwapBuffers();

}

void
init(void)
{
  GLfloat light_diffuse[] = {1.0, 1.0, 1.0, 1.0};  /* Grey diffuse light. */
  GLfloat light_position[] = {1.0, 1.0, 1.0, 0.0};  /* Infinite light location. */

  /* Enable a single OpenGL light. */
  glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
  glLightfv(GL_LIGHT0, GL_POSITION, light_position);
  glEnable(GL_LIGHT0);
  glEnable(GL_LIGHTING);

  /* Use depth buffering for hidden surface elimination. */
  glEnable(GL_DEPTH_TEST);

  /* Setup the view of the image. */
  glMatrixMode(GL_PROJECTION);
  gluPerspective( /* field of view in degree */ 20.0,
    /* aspect ratio */ 1.0,
    /* Z near */ 1.0, /* Z far */ 5.0);
  glMatrixMode(GL_MODELVIEW);
  gluLookAt(0.0, 0.0, 5.0,  /* eye is at (0,0,5) */
    0.0, 0.0, 0.0,      /* center is at (0,0,0) */
    0.0, 1.0, 0.);      /* up is in positive Y direction */

  /* Adjust object position to be asthetic angle. */
  glRotatef(30, 0.0, 1.0, 0.0);
  glScalef(2.2, 2.2, 2.2);
}

int main(int argc, char** argv)
{
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(300,100);
    glutInitWindowSize(400,400);
    glutCreateWindow("Lowpolybunny");
    glutDisplayFunc(display);
    init();
    glutMainLoop();
}