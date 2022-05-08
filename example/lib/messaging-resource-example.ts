import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as chime from 'cdk-amazon-chime-resources';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { v4 as uuidv4 } from 'uuid';

export class MessagingExample extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const appInstance = new chime.MessagingAppInstance(this, 'appInstance', {
      name: 'MessagingAppInstanceExample',
    });

    const channelFlowLambdaRole = new iam.Role(this, 'channelFlowLambdaRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      inlinePolicies: {
        ['chimePolicy']: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              resources: [
                `arn:aws:chime:${this.region}:${this.account}:app-instance/*`,
              ],
              actions: ['chime:ChannelFlowCallback'],
            }),
          ],
        }),
      },
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName(
          'service-role/AWSLambdaBasicExecutionRole',
        ),
      ],
    });

    const channelFlowHandler = new Function(this, 'channelFlowHandler', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'channelFlowHandler.lambda_handler',
      code: Code.fromAsset('src'),
      role: channelFlowLambdaRole,
    });

    channelFlowHandler.addPermission('Chime Resource Policy', {
      principal: new iam.ServicePrincipal('chime.amazonaws.com'),
      sourceArn: `arn:aws:chime:${this.region}:${this.account}:app-instance/*`,
      sourceAccount: `${this.account}`,
    });

    const channelFlow = new chime.ChannelFlow(this, 'channelFlow', {
      appInstanceArn: appInstance.appInstanceArn,
      processors: [
        {
          name: 'channelFlowName',
          configuration: {
            lambda: {
              resourceArn: channelFlowHandler.functionArn,
              invocationType: chime.InvocationType.ASYNC,
            },
          },
          executionOrder: 1,
          fallbackAction: chime.FallbackAction.ABORT,
        },
      ],
      clientRequestToken: uuidv4(),
    });

    new CfnOutput(this, 'appInstanceArn', {
      value: appInstance.appInstanceArn,
    });

    new CfnOutput(this, 'channelFlowArn', {
      value: channelFlow.channelFlowArn,
    });
  }
}
