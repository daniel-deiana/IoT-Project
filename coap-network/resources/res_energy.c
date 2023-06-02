#include "contiki.h"
#include "coap-engine.h"
#include "dev/leds.h"

#include <string.h>
#define CMD_LEN 128
/* Log configuration */
#include "sys/log.h"
#define LOG_MODULE "App"
#define LOG_LEVEL LOG_LEVEL_APP
static int status = 0;

static void res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset);

void parseAndConvert(const uint8_t* data, size_t dataSize, char* outputString, size_t outputSize) {
    size_t i;
    for (i = 0; i < dataSize && i < outputSize - 1; i++) {
        outputString[i] = (char)data[i];
    }
    outputString[i] = '\0'; 
}

/* A simple actuator example, depending on the color query parameter and post variable mode, corresponding led is activated or deactivated */
RESOURCE(res_energy,
         "title=\"energy:?action=shutdown|open \";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, 
					uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
	
	// const char *action = NULL;
  	const uint8_t * chunk;
	char str[CMD_LEN] = "";
	char command[64] = "";
    

  	int len = coap_get_payload(request,&chunk);
    parseAndConvert(chunk,len,str,CMD_LEN);


    printf("valore del payload %s",chunk);

	sscanf(str,"<?xml version='1.0' encoding='UTF-8' ?><cmd> %s </cmd>" ,command);	
    printf("command: %s\n",command);

	coap_set_status_code(response, CHANGED_2_04);

	if (strcmp(command, "open") == 0 && status == 0) {
		leds_set(LEDS_GREEN);
		status = 1;
	}
	else if (strcmp(command,"shutdown") == 0 && status == 1){
		leds_set(LEDS_RED);
		status = 0;
	}
	else {
		printf("Actuator - action not allowed \n");
		coap_set_status_code(response, BAD_REQUEST_4_00);
	}
}
