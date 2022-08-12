#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for(int t = 0; t < candidate_count; t++)//need to find a way to get int voter_count in this struct
    {
        if(strcmp(name, candidates[t].name) == 0)//needto find a way for .name and .votes also names
        {
            candidates[t].votes++;
            return true;
        }
    }
    return false;
}


// Print the winner (or winners) of the election
void print_winner(void)//be able to do ties
{
    // TODO
    int temp=0;

    for(int i = 0; i < candidate_count; i++)
    {
        if(candidates[i].votes > temp)
        {
            temp = candidates[i].votes;
        }
    }

    for(int j=0; j<candidate_count; j++)
    {
        if(candidates[j].votes == temp)
        {
            printf("%s\n",candidates[j].name);
        }
    }

    return;
}
