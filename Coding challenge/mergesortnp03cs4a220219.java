import java.util.Scanner;

public class mergesortnp03cs4a220219{
    void merge(int arr[], int p, int q, int r){
        int num1 = q- p + 1;
        int num2 = r - q;
        int A[] = new int[num1];
        int B[] = new int[num2];
        for (int k = 0; k < num1; ++k)
            A[k] = arr[p + k];
        for (int j = 0; j < num2; ++j)
            B[j] = arr[q + 1 + j];


        int k = 0, j = 0;


        int S = p;
        while (k < num1 && j < num2) {
            if (A[k] <= B[j]) {
                arr[S] = A[k];
                k++;
            }
            else {
                arr[S] = B[j];
                j++;
            }
            S++;
        }


        while (k < num1) {
            arr[S] = A[k];
            k++;
            S++;
        }


        while (j < num2) {
            arr[S] = B[j];
            j++;
            S++;
        }
    }


    void mergesortnp03cs4a220219(int arr[], int p, int r)
    {
        if (p < r) {
            int q = p + (r - p) / 2;
            mergesortnp03cs4a220219 (arr, p, q);
            mergesortnp03cs4a220219(arr, q + 1, r);
            merge(arr, p, q, r);
        }
    }


    static void printArray(int arr[])
    {
        int c = arr.length;
        for (int k = 0; k < c; ++k)
            System.out.print(arr[k] + " ");
        System.out.println();
    }

    public static void main(String args[])
    {
        int size,k;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number of elements in the array:");
        size = s.nextInt();
        int arr[]= new int[size];;
        System.out.println("Enter "+size+" elements ");
        for( k=0; k < size; k++)
        {
            arr[k] = s.nextInt();
        }

        System.out.println("Given Array");
        printArray(arr);

        mergesortnp03cs4a220219 ab = new mergesortnp03cs4a220219();
        ab.mergesortnp03cs4a220219(arr, 0, arr.length - 1);

        System.out.println("\nMain array");
        printArray(arr);
    }
}