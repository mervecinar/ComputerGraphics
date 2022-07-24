/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hw;


import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class DrawCircle extends JFrame {
    public DrawCircle ( int b)
    {
        setSize (500,500);
        setResizable (false);
        setContentPane (new JPanel ()
        {
            public void paint (Graphics g)
            {
                g.setColor (Color.BLUE);
                g.drawOval(50, 50, 2*b, 2*b);
             }
         }
    );
          setVisible (true);
}}