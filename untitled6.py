import java.util.HashSet; 
import java.util.Scanner;
 import java.util.Set; 
public class Solution { 
	private static Scanner sc; 
	static int to = 1; 
	public static void main(String[] args) { 
	sc = new Scanner(System.in); 
	int t sc.nextInt(); sc.nextLine(); 
	while(t-- > 0) {
	solve(); } }
	
private static void solve() {
int size sc.nextInt(); 
int[][] mat = new int[size][size]; 
int k=0;
for(int i =0; i< mat.length; i++){
        for(int j=0; j<mat[i].length; j++)
        { mat[i][j]=sc.extInt();
         if(i==j) k +=mat[i][j]; }}
