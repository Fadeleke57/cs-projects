/*
 * Player.java
 * 
 * Computer Science 112, Boston University
 * 
 * created by: Farouk, fadeleke@bu.edu
 */

import java.util.*;

public class Player {
    private String name;
    private Card[] hand;
    private int numCards;

    /* a constructor that takes a single parameter for the name of the player.*/
    public Player(String name) {
        this.name = name;
        this.numCards = 0;
        this.hand = new Card[Blackjack.MAX_CARDS_PER_PLAYER];
    }
    /*an accessor named getName that returns the player’s name. */
    public String getName() {
        return this.name;
    }
    /*an accessor named getNumCards that returns the current number of cards in the player’s hand. */
    public int getNumCards() {
        int count = 0;
        for (int i = 0; i < Blackjack.MAX_CARDS_PER_PLAYER; i++) {
            if (this.hand[i] != null) {
                count ++;
            }
        }
        return count;
    }
    /*a toString method that just returns the player’s name. */
    public String toString() {
        return getName();
    }
    /* a mutator named addCard that takes a Card object as a parameter and adds the specified card to the player’s hand, filling the array from left to right.*/
    public void addCard(Card Card) {
        if (Card == null || getNumCards() == Blackjack.MAX_CARDS_PER_PLAYER) {
            throw new IllegalArgumentException();
        } 
        else {
            this.numCards ++;
            for (int i = 0; i < this.numCards; i++) {
                if (this.hand[i] == null) {
                    this.hand[i] = Card;
                }   
            }
        }
    }
    /*an accessor named getCard that takes an integer index as a parameter and returns the Card at the specified position in the player’s hand, without actually removing the card from the hand. */
    public Card getCard(int index) {
        if (this.hand[index] == null || index < 0 || index > Blackjack.MAX_CARDS_PER_PLAYER) {
            throw new IllegalArgumentException();
        } 
        else {
            return this.hand[index];
        }
    }
    /*an accessor method named getHandValue that computes and returns the total value of the player’s current hand – i.e., the sum of the values of the individual cards. */
    public int getHandValue() {

        int sum = 0;
        for (int i = 0; i < getNumCards(); i ++) {
            if (this.hand[i].isAce() == false) {
                sum += this.hand[i].getValue();
            }
        }

        int ACElimit = 1;
        for (int i = 0; i < getNumCards(); i ++) {
            if (this.hand[i].isAce() == true && sum + 11 <= 21 && ACElimit == 1 ) {
               sum += 11; 
               ACElimit--;
            } 
            else if (this.hand[i].isAce() == true && sum + 11 > 21 && ACElimit == 1) {
                sum += this.hand[i].getValue();
            }
        }
        return sum;

    }   
    /* an accessor method named printHand that prints the current contents of the player’s hand, followed by the value of the player’s hand.*/
    public void printHand() {
        String s = "";
        for (int i = 0; i < getNumCards(); i ++) {
            s +=this.hand[i] + "  ";
        }
        s +="(value = " + getHandValue() + ")";
        System.out.println(s);
    }
    /*an accessor method named hasBlackjack that returns true if the player has Blackjack (a two-card hand with a value of 21), and false otherwise.  */
    public boolean hasBlackjack() {
        if (getNumCards() == 2 && getHandValue() == 21) {
            return true;
        }
        else {
            return false;
        }
    }
    /* an accessor method called wantsHit that should return true if the player wants another hit, and false if the player does not want another hit.*/
    public boolean wantsHit(Scanner hit, Player opponentPlayer) {
        Scanner console = hit;
        System.out.print("Want another hit, " + getName() + " (y/n)? ");
        String answer = console.nextLine();
    

        if (answer.equals("y") || answer.equals("Y")) {
            return true;
        } 
        else {
            return false;
        } 
    }
    /*a mutator method called discardCards that should get rid of all of the cards in the player’s hand, to prepare for a new round of the game. */
    public void discardCards() {
        for (int i = 0; i < Blackjack.MAX_CARDS_PER_PLAYER; i++) {
            this.hand[i] = null;
        }
        this.numCards = 0;
    }

    public static void main(String[] args) {
        int a = 7;
        double c = a/2;
        System.out.println("a =" + a + " c = " + c);

    }

} 
