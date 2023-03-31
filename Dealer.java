/*
 * Dealer.java
 * 
 * Computer Science 112, Boston University
 * 
 * created by: Farouk, fadeleke@bu.edu
 */

import java.util.*;


public class Dealer extends Player {

    private boolean firstCard;

    /*constructor, which takes no parameters.*/
    public Dealer() {
        super("dealer");
        this.firstCard = false;
    }

    /* a mutator method called revealFirstCard that takes no 
    parameters and changes the value of the called object’s boolean field 
    to indicate that the dealer’s first card should now be revealed.*/
    public boolean revealFirstCard() {
        this.firstCard = true;
        return this.firstCard;
    }

    /*a printHand method that overrides the inherited version of that method. */
    public void printHand() {
        String s = "";
        if (this.firstCard == false) {
            s += "XX  ";
        for (int i = 1; i < getNumCards(); i ++) {
            s += getCard(i) + "  ";
        } 
        System.out.println(s);
        }

        else {
            for (int i = 0; i < getNumCards(); i ++) {
                s += getCard(i) + "  ";
            }
            s += "(value = " + getHandValue() + ")";
            System.out.println(s);
        }
    }
    /*a wantsHit method that overrides the inherited version of that method. This version 
    of the method should determine if the dealer should give herself another hit, and return true or false accordingly.  */
    public boolean wantsHit(Scanner hit, Player opponentPlayer) {

        if (opponentPlayer.getHandValue() < 17 && this.getHandValue() <= opponentPlayer.getHandValue()) {
            return true;
        }
        else if (opponentPlayer.getHandValue() >= 17 && this.getHandValue() < opponentPlayer.getHandValue() && opponentPlayer.hasBlackjack() == false) {
            return true;
        }
        else {
            return false;
        }

    }
    /* a discardCards method that overrides the inherited version of that method.*/
    public void discardCards() {
        super.discardCards();
        this.firstCard = false;
    }

    public static void ShiftRight(int[] values) {
        for (int i = 1; i <values.length; i++) {
            values[i] = values [i -1];
        }
        values[0] = values[values.length -1];

    }

    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = s1;
        String s3 = new String( "hello" );
        String s4 = "hello";
        String s5 = new String( "hello" );
        s1 = "hello world";

        System.out.println(s4 == s2);
        System.out.println(10/5.0);
    
}

}
