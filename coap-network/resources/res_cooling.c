#include "contiki.h"
#include "coap-engine.h"
#include "dev/leds.h"

#include <string.h>

/* Log configuration */
#define CMD_LEN 256
#include "sys/log.h"
#define LOG_MODULE "App"
#define LOG_LEVEL LOG_LEVEL_APP
static int status = 0;


int GetXmlTagValue(char *pResBuf, char *pTag, char *pTagValue)
{
    int len=0, pos = 0;
    char openTag[100] = {0}; //Opening Tag
    char closeTag[100] = {0};//Closing Tag
    int posOpenTag=0, posClosingTag=0;
    //check enter buffer
    len = strlen(pResBuf);
    if (len<=0)
    {
        return -1;
    }
    //Create Opening Tag
    memset(openTag, 0, sizeof(openTag));
    strcpy(openTag, "<");
    strcat(openTag, pTag);
    strcat(openTag, ">");
    //Create Closing tag
    memset(closeTag, 0, sizeof(closeTag));
    strcpy(closeTag, "</");
    strcat(closeTag, pTag);
    strcat(closeTag, ">");
    //Get len of open and close tag
    const int lenOpenTag = strlen(openTag);
    const int lenCloseTag = strlen(closeTag);
    //Get Opening tag position
    for (pos=0; pos<len; pos++)
    {
        if ( !memcmp(openTag,(pResBuf+pos),lenOpenTag))
        {
            posOpenTag = pos;
            break;
        }
    }
    //Get closing tag position
    for (pos=0; pos<len; pos++)
    {
        if ( !memcmp(closeTag,(pResBuf+pos),lenCloseTag) )
        {
            posClosingTag = pos;
            break;
        }
    }
    //get the tag value
    if ( (posOpenTag !=0) && (posClosingTag !=0) )
    {
        const int lenTagVal = posClosingTag-posOpenTag-lenOpenTag;
        const char * const pStartPosTagVal = pResBuf+posOpenTag+lenOpenTag;
        if (lenTagVal)
        {
            //Get tag value
            memcpy(pTagValue,pStartPosTagVal, lenTagVal);
            if (strlen(pTagValue))
            {
                return 1;
            }
        }
    }
    return -1;
}

void parseAndConvert(const uint8_t* data, size_t dataSize, char* outputString, size_t outputSize) {
    size_t i;
    for (i = 0; i < dataSize && i < outputSize - 1; i++) {
        outputString[i] = (char)data[i];
    }
    outputString[i] = '\0'; 
}

static void res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset);

/* A simple actuator example, depending on the color query parameter and post variable mode, corresponding led is activated or deactivated */
RESOURCE(res_cooling,
         "title=\"LEDs:?action=activate|deactivate\";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
	
  	// const char *action = NULL;
  	const uint8_t * chunk;
	char str[CMD_LEN] = "";
	char command[64] = "";
    

  	int len = coap_get_payload(request,&chunk);
    parseAndConvert(chunk,len,str,CMD_LEN);


    printf("valore del payload %s",chunk);

	sscanf(str,"<?xml version='1.0' encoding='UTF-8' ?><cmd> %s </cmd>" ,command);	
    printf("command: %s.\n",command);

	coap_set_status_code(response, CHANGED_2_04);

	// printf("la stringa e %s", str);

	if (strcmp(command, "activate") == 0 && status == 0) {
		leds_set(LEDS_YELLOW);
		status = 1;
	}
	else if (strcmp(command, "deactivate") == 0 && status == 1){
		leds_set(LEDS_RED);
		status = 0;
	}
	else {
		printf("Actuator - action not allowed \n");
		coap_set_status_code(response, BAD_REQUEST_4_00);
	}
}
