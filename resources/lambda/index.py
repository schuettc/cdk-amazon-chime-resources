import phonenumbers
import sipmediaapp
import siprule
import voiceconnectors
import boto3
import botocore


def handler(event, context):
    print(event)
    print(f"Boto3 Version: {boto3.__version__}")
    print(f"BotoCore Version: {botocore.__version__}")
    responseData = {}
    properties = event["ResourceProperties"]["properties"]
    uid = event["ResourceProperties"]["uid"]
    resource_type = event["ResourceProperties"]["resourceType"]
    if event["RequestType"] == "Create":
        if resource_type == "PhoneNumber":
            try:
                responseData["phoneNumber"] = phonenumbers.getPhoneNumber(uid, **properties)
                return {"PhysicalResourceId": uid, "Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "VoiceConnector":
            try:
                responseData["voiceConnectorId"] = voiceconnectors.create_voiceconnector(uid, **properties)
                return {"PhysicalResourceId": uid, "Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "SMA":
            try:
                responseData["sipMediaAppId"] = sipmediaapp.createSipMediaApp(uid, **properties)
                return {"PhysicalResourceId": uid, "Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "SMARule":
            try:
                responseData["sipRuleId"] = siprule.createSipRule(uid, **properties)
                return {"PhysicalResourceId": uid, "Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)

    elif event["RequestType"] == "Delete":
        if resource_type == "PhoneNumber":
            try:
                responseData["phoneNumber"] = phonenumbers.deletePhoneNumber(uid)
                return {"Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "VoiceConnector":
            try:
                responseData = voiceconnectors.delete_voiceconnector(uid)
                return {"Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "SMA":
            try:
                responseData["sipMediaAppId"] = sipmediaapp.deleteSipMediaApp(uid)
                return {"Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)
        if resource_type == "SMARule":
            try:
                responseData["sipRuleId"] = siprule.deleteSipRule(uid, **properties)
                return {"Data": responseData}
            except Exception as e:
                error = {"error": f"Exception thrown: {e}"}
                print(error)
                raise Exception(error)

    else:
        responseData = {"Message": "Update is no-op. Returning success status."}
        return {"PhysicalResourceId": uid, "Data": responseData}
