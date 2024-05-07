#include <stdio.h>

int main() {
    // Open a file for writing
    FILE *fp = fopen("example.json", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write JSON data to the file
    fprintf(fp, "{\n");
    fprintf(fp, "    \"name\": \"John Doe\",\n");
    fprintf(fp, "    \"age\": 30,\n");
    fprintf(fp, "    \"city\": \"New York\"\n");
    fprintf(fp, "}\n");

    // Close the file
    fclose(fp);

    printf("JSON file created successfully!\n");

    return 0;
}