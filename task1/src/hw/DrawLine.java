package hw;

import java.awt.*;
import javax.swing.*;
import java.awt.geom.Line2D;
  import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;
public class DrawLine extends JFrame {
    
        public DrawLine ( int b)
    {
        setSize (500,500);
        setResizable (false);
        setContentPane (new JPanel ()
        {
            public void paint(Graphics g)
    {

         g.setColor (Color.PINK);
          g.drawLine(50, 50, b, b);
    }
         }
    );
          setVisible (true);
}
  

}
  
