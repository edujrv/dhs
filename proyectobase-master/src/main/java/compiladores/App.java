package compiladores;

import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

public class App {

    public static void main(String[] args) throws Exception {
        // create a CharStream that reads from file
        CharStream input = CharStreams.fromFileName("src/entrada.txt");
        // CharStream input = CharStreams.fromFileName("src/datos.txt");

        // create a lexer that feeds off of input CharStream
        compiladorLexer lexer = new compiladorLexer(input);
        
        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        
        // create a parser that feeds off the tokens buffer
        compiladorParser parser = new compiladorParser(tokens);

        // create Listener
        // compiladorBaseListener escucha = new MiListener();

        // Conecto el objeto con Listeners al parser
        // parser.addParseListener(escucha);

        // Solicito al parser que comience indicando una regla gramatical
        // En este caso la regla es el simbolo inicial
        // parser.horas();
    
        // ParseTree tree = parser.s();

        // Conectamos el visitor
        // MiVisitor<ParseTree> visitor = new MiVisitor<>();
        // visitor.visit(tree);
        // System.out.println(visitor);
        // System.out.println(visitor.getErrorNodes());
        // Imprime el arbol obtenido
        // System.out.println(tree.toStringTree(parser));
        // System.out.println(escucha);

        // Caminante walker = new Caminante();
        // walker.visit(tree);
        // System.out.println(walker);
        // System.out.println(walker.getErrorNodes());
    }
}
