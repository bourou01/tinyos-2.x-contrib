#include "DSN.h"

/**
 * This modules detects dsn commands with following format:
 * key value1 value2 value3 ...
 * 
 * commands with too many parameters, non-integer parameters are not detected
 * 
 * module parameters:
 * key: command string to detect
 * valueType: type of parameters (only integers)
 * maxValueCount: upper bound of parameter count
 * 
 * --> don't forget to wire every new DsnCommand to the DSNC component !
 * 
 * @author Roman Lim <rlim@ee.ethz.ch>
 * 
 */
 
generic module DsnCommandC(
	uint8_t key[], 
	typedef valueType @integer(),
	uint8_t maxValueCount)
{
  provides interface DsnCommand<valueType>;
  uses interface DSN;	
}

implementation
{
	valueType values[maxValueCount];
	
	enum {
		SEPARATOR=' ',
		LOG_DELIMITER2='\r',
	};
	
	event void DSN.receive(void *msg, uint8_t len) {
		uint8_t i=0, v=0;	
		uint8_t * cmd = (uint8_t*)msg;
		
		/*
		call DSN.logInt(len);
		call DSN.appendLog("CMD[%i]:");
		call DSN.log(msg);
		*/
		
		while (key[i]!=0 && key[i]==cmd[i]) {
			i++;
		}
		if (key[i]==0) {
			if (cmd[i]==LOG_DELIMITER || cmd[i]==LOG_DELIMITER2) {
				signal DsnCommand.detected(NULL, 0);
			}
			else if ((cmd[i]==SEPARATOR) && cmd[i+1]>='0' && cmd[i+1]<='9') {
				i++;
				values[0]=0;
				while (i<len) {
					if (cmd[i]==SEPARATOR) {
						v++;
						if (v>=maxValueCount)
							return;
						else {
							values[v]=0;
						}
					}
					else if ( cmd[i]>='0' && cmd[i]<='9') {
						values[v]=values[v]*10 + cmd[i]-'0';
					}
					else if (cmd[i]==LOG_DELIMITER || cmd[i]==LOG_DELIMITER2)
						break;
					else
						return;
					i++;
				}
				signal DsnCommand.detected((valueType *) &values[0], ++v);
			}
		}
  	}
}