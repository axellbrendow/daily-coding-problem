// https://www.hackerrank.com/challenges/java-vistor-pattern/problem

import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.ArrayList;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {

    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {

    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {

    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis {
    public abstract int getResult();

    public abstract void visitNode(TreeNode node);

    public abstract void visitLeaf(TreeLeaf leaf);

}

class SumInLeavesVisitor extends TreeVis {
    private int sum = 0;

    public int getResult() {
        return sum;
    }

    public void visitNode(TreeNode node) {
    }

    public void visitLeaf(TreeLeaf leaf) {
        sum += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private long product = 1;

    private static final int MOD = (int) Math.pow(10, 9) + 7;

    public int getResult() {
        return (int) product;
    }

    public void visitGenericNode(Tree node) {
        if (node.getColor() == Color.RED) {
            product = (product * node.getValue()) % MOD;
        }
    }

    public void visitNode(TreeNode node) {
        visitGenericNode(node);
    }

    public void visitLeaf(TreeLeaf leaf) {
        visitGenericNode(leaf);
    }
}

class FancyVisitor extends TreeVis {
    private int sumOfNonLeafNodesInEvenDepth = 0;
    private int sumOfGreenLeafNodes = 0;

    public int getResult() {
        return Math.abs(sumOfNonLeafNodesInEvenDepth - sumOfGreenLeafNodes);
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0) {
            sumOfNonLeafNodesInEvenDepth += node.getValue();
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.GREEN) {
            sumOfGreenLeafNodes += leaf.getValue();
        }
    }
}

public class JavaVisitorPattern {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    private static String readLine() {
        try {
            return reader.readLine();
        } catch (Exception ex) {
            return null;
        }
    }

    private static int[] readIntegers(int[] integers) {
        String line = readLine();
        if (line == null || line.trim().length() == 0)
            return null;

        try (Scanner scan = new Scanner(line)) {
            for (int i = 0; i < integers.length; i++) {
                integers[i] = scan.nextInt();
            }
        }
        return integers;
    }

    private static int[] readIntegers(int n) {
        return readIntegers(new int[n]);
    }

    private static Tree buildTree(
            int parentIndex,
            int nodeIndex,
            int depth,
            int[] values,
            int[] colors,
            HashMap<Integer, List<Integer>> edges) {
        List<Integer> children = edges.get(nodeIndex);

        // Edges are "bidirectional", that's why <= 1 and not <= 0
        if (children.size() <= 1) {
            return new TreeLeaf(
                    values[nodeIndex],
                    colors[nodeIndex] == 0 ? Color.RED : Color.GREEN,
                    depth);
        }

        TreeNode node = new TreeNode(
                values[nodeIndex],
                colors[nodeIndex] == 0 ? Color.RED : Color.GREEN,
                depth);

        for (int childIndex : children) {
            if (childIndex == parentIndex)
                continue;
            node.addChild(buildTree(nodeIndex, childIndex, depth + 1, values, colors, edges));
        }

        return node;
    }

    public static Tree solve() {
        int n = Integer.parseInt(readLine());
        int[] values = readIntegers(n);
        int[] colors = readIntegers(n);

        int[] edge = new int[2];
        HashMap<Integer, List<Integer>> edges = new HashMap<Integer, List<Integer>>();

        while (readIntegers(edge) != null) {
            // In this question, it is not guaranteed that this relation is
            // parent-child or child-parent, it's part of the question to find out
            int node1Index = edge[0] - 1;
            int node2Index = edge[1] - 1;

            if (!edges.containsKey(node1Index)) {
                edges.put(node1Index, new ArrayList<Integer>());
            }
            edges.get(node1Index).add(node2Index);

            if (!edges.containsKey(node2Index)) {
                edges.put(node2Index, new ArrayList<Integer>());
            }
            edges.get(node2Index).add(node1Index);
        }

        return buildTree(-1, 0, 0, values, colors, edges);
    }

    public static void main(String[] args) {
        Tree root = solve();
        SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
        ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
        FancyVisitor vis3 = new FancyVisitor();

        root.accept(vis1);
        root.accept(vis2);
        root.accept(vis3);

        int res1 = vis1.getResult();
        int res2 = vis2.getResult();
        int res3 = vis3.getResult();

        System.out.println(res1);
        System.out.println(res2);
        System.out.println(res3);
    }
}
