// Implements a dictionary's functionality
#include <ctype.h>

#include <stdio.h>

#include <cs50.h>

#include <string.h>

#include <stdlib.h>

#include <strings.h>

#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
unsigned int hashed;
unsigned int word_count;

// Number of buckets in hash table
const unsigned int N = 65536;// 2^16

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    hashed = hash(word);
    node *temp_2 = table[hashed];
    while(temp_2 != NULL)
    {
        if(strcasecmp(word, temp_2->word) == 0)
        {
            return true;
        }
        temp_2 = temp_2->next;
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //TODO
    unsigned long index = 5381;
    int c = 0;
    while ((c = tolower(*word++)))
    {
        index = ((index << 5) + index) + c;
    }
    return index % N;

}


// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    FILE *temp = fopen(dictionary, "r");
    if (temp == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(temp, "%s", word) != EOF)
    {
        node *t = malloc(sizeof(node));
        if (t == NULL)
        {
            return false;
        }
        strcpy(t->word, word);
        hashed = hash(word);
        t->next = table[hashed];
        table[hashed] = t;
        word_count++;
    }
    fclose(temp); //success
    return true;
}


// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if(word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for(int i = 0; i < N; i++) //buckets
    {
        node *temp_2 = table[i];
        while(temp_2){
            node *B = temp_2;
            temp_2 = temp_2->next;
            free(B);
        }
        if (i == N - 1 && temp_2 == NULL)
        {
            return true;
        }
    }
    return false;
}