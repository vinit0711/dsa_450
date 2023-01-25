public class ReverseArray {
    
    static void reversetheArray(int[] array) {
        int start = 0;
        int end = array.length - 1;
        int temp;
        while (start < end) {
            temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }

    static void printArray(int arr[]) {
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] );
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5, 6 };
        printArray(array);
        System.out.println("Printing Reverse Array");
        reversetheArray(array);
        printArray(array);
    }
}
