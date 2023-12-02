import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleGUI extends JFrame {

    private JLabel label;
    private JButton button;

    public SimpleGUI() {
        // Set up the JFrame
        super("Simple GUI Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);

        // Create components
        label = new JLabel("Hello, GUI!");
        button = new JButton("Click me");

        // Set up the layout
        JPanel panel = new JPanel();
        panel.add(label);
        panel.add(button);
        add(panel);

        // Add event listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                label.setText("Button clicked!");
            }
        });
    }

    public static void main(String[] args) {
        // Run the GUI in the Event Dispatch Thread (EDT)
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new SimpleGUI().setVisible(true);
            }
        });
    }
}
