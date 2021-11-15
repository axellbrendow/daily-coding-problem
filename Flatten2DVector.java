import java.util.Iterator;

public class Flatten2DVector implements Iterator<Integer>, Iterable<Integer> {
    private int[][] matrix;
    private int i = 0;
    private int j = 0;

    public Flatten2DVector(int[][] matrix) {
        this.matrix = matrix;
    }

    @Override
    public boolean hasNext() {
        return i < matrix.length && j < matrix[i].length;
    }

    @Override
    public Integer next() {
        var val = matrix[i][j++];
        if (j >= matrix[i].length) {
            j = 0;
            i++;
        }
        return val;
    }

    @Override
    public Flatten2DVector iterator() { return new Flatten2DVector(matrix); }

    public static void main(String[] args) {
        var matrix = new int[][] {
            new int[] {1,2},
            new int[] {3},
            new int[] {4,5,6},
        };

        // while (iterator.hasNext()) System.out.println(iterator.next());

        for (var elem : new Flatten2DVector(matrix))
            System.out.println(elem);
    }
}
