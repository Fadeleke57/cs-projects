/*
 * Card.java
 *
 * A blueprint class for objects that represent a single playing card
 * that has a rank and a suit.
 * 
 * starter code: CS 112 Staff (cs112-staff@cs.bu.edu)
 * completed by: Farouk Adeleke fadeleke@bu.edu
 */

public class Card {
    /* constants for the ranks of non-numeric cards */
    public static final int ACE = 1;
    public static final int JACK = 11;
    public static final int QUEEN = 12;
    public static final int KING = 13;
    
    /* other constants for the ranks */
    public static final int FIRST_RANK = 1;
    public static final int LAST_RANK = 13;
    
    /* 
     * class-constant array containing the string representations
     * of all of the card ranks. 
     * The string for the numeric rank r is given by RANK_STRINGS[r].
     */
    public static final String[] RANK_STRINGS = {
      null, "A", "2", "3", "4", "5", "6",
      "7", "8", "9", "10", "J", "Q", "K"
    };
    
    /* 
     * class-constant array containing the char representations
     * of all of the possible suits.
     */
    public static final char[] SUITS = {'C', 'D', 'H', 'S'};

    
    /* Put the rest of the class definition below. */

    /* 
     * taking a rank string as its only parameter and returning the 
     * corresponding integer rank. In other words, the method should 
     * find and return the index of the specified rank string in the 
     * RANK_STRINGS array.
     */
    public static int rankNumFor(String s) {
      if (s == null) {
        return -1;
      }
      int count = 0;
      int pos = 0;
      for (int i = 0; i < RANK_STRINGS.length; i++ ) {
        if (s.equals(RANK_STRINGS[i])) {
            count ++;
            pos = i;
        }
      } 
      if (count == 1) {
        return pos;
      }
      else {
        return -1;
      }
    }

    /*takes a single-character representation of a card’s suit and returns
     true if that suit is valid (i.e., if it is one of the values in the SUITS 
     array), and false otherwise. */

    public static boolean isValidSuit(char s) {
        int count = 0;
        for (int i = 0; i < SUITS.length; i++) {
          if (s == SUITS[i]) {
            count ++; 
          }
        } 
        if (count >=1) {
          return true;
        } 
        else {
          return false;
        }
    }

    private int rank;
    private char suit;

    /* a constructor that takes two parameters: an integer specifying the card’s rank, 
    and a single character (a char) specifying the card’s suit (in that order). */
    public Card(int r, char s) {
      if (isValidSuit(s) == true && r >= 1 && r <= 13) {
        this.suit = s;
        this.rank = r;
      } 
      else {
        throw new IllegalArgumentException();
    }
  }

      /*a constructor that takes a single parameter: a two- or three-character 
      string that specifies the card to be created. */
    public Card(String s) {
        if (s == null) {
          throw new IllegalArgumentException();
        } 
        if (s.length() > 3 || s.length() < 2) {
          throw new IllegalArgumentException();
        }
        else {
          String s2 = s.substring(0, s.length()-1);
          char tempS = s.charAt(s.length()-1);
          if (rankNumFor(s2) == -1 || isValidSuit(tempS) == false) {
            throw new IllegalArgumentException();
          } 
          else {
            this.rank = rankNumFor(s2);
            this.suit = tempS;
          }
        }   
    }
    
    /* returns the integer representing the Card object’s rank*/

    public int getRank() {
      return this.rank;
    }

    /* returns the char representing the Card object’s suit. */

    public char getSuit() {
      return this.suit;
    }

    /* returns true if the Card is an Ace and false if it is not. */

    public boolean isAce() {
      if (this.rank == ACE) {
        return true;
      }
      return false;
    }

    /* returns true if the Card is a face card (Jack, Queen, or King) 
    and and false if it is not.*/

    public boolean isFaceCard() {
        if (this.rank == JACK || this.rank == QUEEN || this.rank == KING ) {
          return true;
        }
        return false;
    }

    /*returns the Card object’s value. If the card is a face card, then it 
    should return a value of 10.Otherwise, it should return the card’s rank. */

    public int getValue() {
      if (isFaceCard() == true) {
        return 10;
      } 
      else {
        return this.rank;
      }

    }

    /* returns a String representation of the Card object that can be used when 
    printing it or concatenating it to a String.*/

    public String toString() {
      String s = RANK_STRINGS[this.rank] + "" + this.suit;
      return s;
    }

    /*takes a Card object as a parameter and determines if it is has the same suit 
    as the called object, returning true if they have the same suit and false if 
    they do not have the same suit.*/

    public boolean sameSuitAs(Card other) {
      return (other != null && this.suit == other.suit);
      
    }

    /*takes a Card object as a parameter and determines if it is equivalent to the 
    called object, returning true if it is equivalent and false if it is not equivalent.*/

    public boolean equals(Card other) {
      return (other != null && this.suit == other.suit && this.rank == other.rank);
    }

    public static void main(String[] args) {

    }


}

