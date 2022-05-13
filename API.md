# API Reference <a name="API Reference" id="api-reference"></a>

## Constructs <a name="Constructs" id="constructs"></a>

### ChimePhoneNumber <a name="cdk-amazon-chime-resources.ChimePhoneNumber" id="cdkamazonchimeresourceschimephonenumber"></a>

#### Initializers <a name="cdk-amazon-chime-resources.ChimePhoneNumber.Initializer" id="cdkamazonchimeresourceschimephonenumberinitializer"></a>

```typescript
import { ChimePhoneNumber } from 'cdk-amazon-chime-resources'

new ChimePhoneNumber(scope: Construct, id: string, props: PhoneNumberProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourceschimephonenumberparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourceschimephonenumberparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourceschimephonenumberparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.PhoneNumberProps`](#cdk-amazon-chime-resources.PhoneNumberProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimePhoneNumber.parameter.scope" id="cdkamazonchimeresourceschimephonenumberparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimePhoneNumber.parameter.id" id="cdkamazonchimeresourceschimephonenumberparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimePhoneNumber.parameter.props" id="cdkamazonchimeresourceschimephonenumberparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.PhoneNumberProps`](#cdk-amazon-chime-resources.PhoneNumberProps)

---

#### Methods <a name="Methods" id="methods"></a>

| **Name** | **Description** |
| --- | --- |
| [`associateWithVoiceConnector`](#cdkamazonchimeresourceschimephonenumberassociatewithvoiceconnector) | *No description.* |

---

##### `associateWithVoiceConnector` <a name="cdk-amazon-chime-resources.ChimePhoneNumber.associateWithVoiceConnector" id="cdkamazonchimeresourceschimephonenumberassociatewithvoiceconnector"></a>

```typescript
public associateWithVoiceConnector(voiceConnectorId: ChimeVoiceConnector)
```

###### `voiceConnectorId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimePhoneNumber.parameter.voiceConnectorId" id="cdkamazonchimeresourceschimephonenumberparametervoiceconnectorid"></a>

- *Type:* [`cdk-amazon-chime-resources.ChimeVoiceConnector`](#cdk-amazon-chime-resources.ChimeVoiceConnector)

---


#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`phoneNumber`](#cdkamazonchimeresourceschimephonenumberpropertyphonenumber)<span title="Required">*</span> | `string` | *No description.* |

---

##### `phoneNumber`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimePhoneNumber.property.phoneNumber" id="cdkamazonchimeresourceschimephonenumberpropertyphonenumber"></a>

```typescript
public readonly phoneNumber: string;
```

- *Type:* `string`

---


### ChimeResources <a name="cdk-amazon-chime-resources.ChimeResources" id="cdkamazonchimeresourceschimeresources"></a>

#### Initializers <a name="cdk-amazon-chime-resources.ChimeResources.Initializer" id="cdkamazonchimeresourceschimeresourcesinitializer"></a>

```typescript
import { ChimeResources } from 'cdk-amazon-chime-resources'

new ChimeResources(scope: Construct, id: string, props: ChimeResourceProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourceschimeresourcesparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourceschimeresourcesparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourceschimeresourcesparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.ChimeResourceProps`](#cdk-amazon-chime-resources.ChimeResourceProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResources.parameter.scope" id="cdkamazonchimeresourceschimeresourcesparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResources.parameter.id" id="cdkamazonchimeresourceschimeresourcesparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResources.parameter.props" id="cdkamazonchimeresourceschimeresourcesparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.ChimeResourceProps`](#cdk-amazon-chime-resources.ChimeResourceProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`chimeCustomResource`](#cdkamazonchimeresourceschimeresourcespropertychimecustomresource)<span title="Required">*</span> | [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource) | *No description.* |
| [`lambda`](#cdkamazonchimeresourceschimeresourcespropertylambda)<span title="Required">*</span> | [`aws-cdk-lib.aws_lambda.IFunction`](#aws-cdk-lib.aws_lambda.IFunction) | *No description.* |

---

##### `chimeCustomResource`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResources.property.chimeCustomResource" id="cdkamazonchimeresourceschimeresourcespropertychimecustomresource"></a>

```typescript
public readonly chimeCustomResource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---

##### `lambda`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResources.property.lambda" id="cdkamazonchimeresourceschimeresourcespropertylambda"></a>

```typescript
public readonly lambda: IFunction;
```

- *Type:* [`aws-cdk-lib.aws_lambda.IFunction`](#aws-cdk-lib.aws_lambda.IFunction)

---


### ChimeSipMediaApp <a name="cdk-amazon-chime-resources.ChimeSipMediaApp" id="cdkamazonchimeresourceschimesipmediaapp"></a>

#### Initializers <a name="cdk-amazon-chime-resources.ChimeSipMediaApp.Initializer" id="cdkamazonchimeresourceschimesipmediaappinitializer"></a>

```typescript
import { ChimeSipMediaApp } from 'cdk-amazon-chime-resources'

new ChimeSipMediaApp(scope: Construct, id: string, props: SipMediaAppProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourceschimesipmediaappparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourceschimesipmediaappparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourceschimesipmediaappparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.SipMediaAppProps`](#cdk-amazon-chime-resources.SipMediaAppProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipMediaApp.parameter.scope" id="cdkamazonchimeresourceschimesipmediaappparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipMediaApp.parameter.id" id="cdkamazonchimeresourceschimesipmediaappparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipMediaApp.parameter.props" id="cdkamazonchimeresourceschimesipmediaappparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.SipMediaAppProps`](#cdk-amazon-chime-resources.SipMediaAppProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`sipMediaAppId`](#cdkamazonchimeresourceschimesipmediaapppropertysipmediaappid)<span title="Required">*</span> | `string` | *No description.* |

---

##### `sipMediaAppId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipMediaApp.property.sipMediaAppId" id="cdkamazonchimeresourceschimesipmediaapppropertysipmediaappid"></a>

```typescript
public readonly sipMediaAppId: string;
```

- *Type:* `string`

---


### ChimeSipRule <a name="cdk-amazon-chime-resources.ChimeSipRule" id="cdkamazonchimeresourceschimesiprule"></a>

#### Initializers <a name="cdk-amazon-chime-resources.ChimeSipRule.Initializer" id="cdkamazonchimeresourceschimesipruleinitializer"></a>

```typescript
import { ChimeSipRule } from 'cdk-amazon-chime-resources'

new ChimeSipRule(scope: Construct, id: string, props: SipRuleProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourceschimesipruleparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourceschimesipruleparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourceschimesipruleparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.SipRuleProps`](#cdk-amazon-chime-resources.SipRuleProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipRule.parameter.scope" id="cdkamazonchimeresourceschimesipruleparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipRule.parameter.id" id="cdkamazonchimeresourceschimesipruleparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipRule.parameter.props" id="cdkamazonchimeresourceschimesipruleparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.SipRuleProps`](#cdk-amazon-chime-resources.SipRuleProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`sipRuleId`](#cdkamazonchimeresourceschimesiprulepropertysipruleid)<span title="Required">*</span> | `string` | *No description.* |

---

##### `sipRuleId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeSipRule.property.sipRuleId" id="cdkamazonchimeresourceschimesiprulepropertysipruleid"></a>

```typescript
public readonly sipRuleId: string;
```

- *Type:* `string`

---


### ChimeVoiceConnector <a name="cdk-amazon-chime-resources.ChimeVoiceConnector" id="cdkamazonchimeresourceschimevoiceconnector"></a>

#### Initializers <a name="cdk-amazon-chime-resources.ChimeVoiceConnector.Initializer" id="cdkamazonchimeresourceschimevoiceconnectorinitializer"></a>

```typescript
import { ChimeVoiceConnector } from 'cdk-amazon-chime-resources'

new ChimeVoiceConnector(scope: Construct, id: string, props: VoiceConnectorProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourceschimevoiceconnectorparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourceschimevoiceconnectorparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourceschimevoiceconnectorparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.VoiceConnectorProps`](#cdk-amazon-chime-resources.VoiceConnectorProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeVoiceConnector.parameter.scope" id="cdkamazonchimeresourceschimevoiceconnectorparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeVoiceConnector.parameter.id" id="cdkamazonchimeresourceschimevoiceconnectorparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeVoiceConnector.parameter.props" id="cdkamazonchimeresourceschimevoiceconnectorparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.VoiceConnectorProps`](#cdk-amazon-chime-resources.VoiceConnectorProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`voiceConnectorId`](#cdkamazonchimeresourceschimevoiceconnectorpropertyvoiceconnectorid)<span title="Required">*</span> | `string` | *No description.* |

---

##### `voiceConnectorId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeVoiceConnector.property.voiceConnectorId" id="cdkamazonchimeresourceschimevoiceconnectorpropertyvoiceconnectorid"></a>

```typescript
public readonly voiceConnectorId: string;
```

- *Type:* `string`

---


### PhoneAssociation <a name="cdk-amazon-chime-resources.PhoneAssociation" id="cdkamazonchimeresourcesphoneassociation"></a>

#### Initializers <a name="cdk-amazon-chime-resources.PhoneAssociation.Initializer" id="cdkamazonchimeresourcesphoneassociationinitializer"></a>

```typescript
import { PhoneAssociation } from 'cdk-amazon-chime-resources'

new PhoneAssociation(scope: Construct, id: string, props: PhoneAssociationProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#cdkamazonchimeresourcesphoneassociationparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#cdkamazonchimeresourcesphoneassociationparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#cdkamazonchimeresourcesphoneassociationparameterprops)<span title="Required">*</span> | [`cdk-amazon-chime-resources.PhoneAssociationProps`](#cdk-amazon-chime-resources.PhoneAssociationProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociation.parameter.scope" id="cdkamazonchimeresourcesphoneassociationparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociation.parameter.id" id="cdkamazonchimeresourcesphoneassociationparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociation.parameter.props" id="cdkamazonchimeresourcesphoneassociationparameterprops"></a>

- *Type:* [`cdk-amazon-chime-resources.PhoneAssociationProps`](#cdk-amazon-chime-resources.PhoneAssociationProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`phoneAssociationResource`](#cdkamazonchimeresourcesphoneassociationpropertyphoneassociationresource)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.AwsCustomResource`](#aws-cdk-lib.custom_resources.AwsCustomResource) | *No description.* |

---

##### `phoneAssociationResource`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociation.property.phoneAssociationResource" id="cdkamazonchimeresourcesphoneassociationpropertyphoneassociationresource"></a>

```typescript
public readonly phoneAssociationResource: AwsCustomResource;
```

- *Type:* [`aws-cdk-lib.custom_resources.AwsCustomResource`](#aws-cdk-lib.custom_resources.AwsCustomResource)

---


## Structs <a name="Structs" id="structs"></a>

### ChimeResourceProps <a name="cdk-amazon-chime-resources.ChimeResourceProps" id="cdkamazonchimeresourceschimeresourceprops"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { ChimeResourceProps } from 'cdk-amazon-chime-resources'

const chimeResourceProps: ChimeResourceProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`account`](#cdkamazonchimeresourceschimeresourcepropspropertyaccount) | `string` | The AWS account ID this resource belongs to. |
| [`environmentFromArn`](#cdkamazonchimeresourceschimeresourcepropspropertyenvironmentfromarn) | `string` | ARN to deduce region and account from. |
| [`physicalName`](#cdkamazonchimeresourceschimeresourcepropspropertyphysicalname) | `string` | The value passed in by users to the physical name prop of the resource. |
| [`region`](#cdkamazonchimeresourceschimeresourcepropspropertyregion) | `string` | The AWS region this resource belongs to. |
| [`properties`](#cdkamazonchimeresourceschimeresourcepropspropertyproperties)<span title="Required">*</span> | {[ key: string ]: `any`} | *No description.* |
| [`resourceType`](#cdkamazonchimeresourceschimeresourcepropspropertyresourcetype)<span title="Required">*</span> | `string` | *No description.* |
| [`uid`](#cdkamazonchimeresourceschimeresourcepropspropertyuid)<span title="Required">*</span> | `string` | *No description.* |

---

##### `account`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.account" id="cdkamazonchimeresourceschimeresourcepropspropertyaccount"></a>

```typescript
public readonly account: string;
```

- *Type:* `string`
- *Default:* the resource is in the same account as the stack it belongs to

The AWS account ID this resource belongs to.

---

##### `environmentFromArn`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.environmentFromArn" id="cdkamazonchimeresourceschimeresourcepropspropertyenvironmentfromarn"></a>

```typescript
public readonly environmentFromArn: string;
```

- *Type:* `string`
- *Default:* take environment from `account`, `region` parameters, or use Stack environment.

ARN to deduce region and account from.

The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources.  Cannot be supplied together with either `account` or `region`.

---

##### `physicalName`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.physicalName" id="cdkamazonchimeresourceschimeresourcepropspropertyphysicalname"></a>

```typescript
public readonly physicalName: string;
```

- *Type:* `string`
- *Default:* The physical name will be allocated by CloudFormation at deployment time

The value passed in by users to the physical name prop of the resource.

`undefined` implies that a physical name will be allocated by    CloudFormation during deployment. - a concrete value implies a specific physical name - `PhysicalName.GENERATE_IF_NEEDED` is a marker that indicates that a physical will only be generated    by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

---

##### `region`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.region" id="cdkamazonchimeresourceschimeresourcepropspropertyregion"></a>

```typescript
public readonly region: string;
```

- *Type:* `string`
- *Default:* the resource is in the same region as the stack it belongs to

The AWS region this resource belongs to.

---

##### `properties`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.properties" id="cdkamazonchimeresourceschimeresourcepropspropertyproperties"></a>

```typescript
public readonly properties: {[ key: string ]: any};
```

- *Type:* {[ key: string ]: `any`}

---

##### `resourceType`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.resourceType" id="cdkamazonchimeresourceschimeresourcepropspropertyresourcetype"></a>

```typescript
public readonly resourceType: string;
```

- *Type:* `string`

---

##### `uid`<sup>Required</sup> <a name="cdk-amazon-chime-resources.ChimeResourceProps.property.uid" id="cdkamazonchimeresourceschimeresourcepropspropertyuid"></a>

```typescript
public readonly uid: string;
```

- *Type:* `string`

---

### Logging <a name="cdk-amazon-chime-resources.Logging" id="cdkamazonchimeresourceslogging"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { Logging } from 'cdk-amazon-chime-resources'

const logging: Logging = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`mediaMetricLogs`](#cdkamazonchimeresourcesloggingpropertymediametriclogs) | `boolean` | *No description.* |
| [`sipLogs`](#cdkamazonchimeresourcesloggingpropertysiplogs) | `boolean` | *No description.* |

---

##### `mediaMetricLogs`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.Logging.property.mediaMetricLogs" id="cdkamazonchimeresourcesloggingpropertymediametriclogs"></a>

```typescript
public readonly mediaMetricLogs: boolean;
```

- *Type:* `boolean`

---

##### `sipLogs`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.Logging.property.sipLogs" id="cdkamazonchimeresourcesloggingpropertysiplogs"></a>

```typescript
public readonly sipLogs: boolean;
```

- *Type:* `boolean`

---

### PhoneAssociationProps <a name="cdk-amazon-chime-resources.PhoneAssociationProps" id="cdkamazonchimeresourcesphoneassociationprops"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { PhoneAssociationProps } from 'cdk-amazon-chime-resources'

const phoneAssociationProps: PhoneAssociationProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`account`](#cdkamazonchimeresourcesphoneassociationpropspropertyaccount) | `string` | The AWS account ID this resource belongs to. |
| [`environmentFromArn`](#cdkamazonchimeresourcesphoneassociationpropspropertyenvironmentfromarn) | `string` | ARN to deduce region and account from. |
| [`physicalName`](#cdkamazonchimeresourcesphoneassociationpropspropertyphysicalname) | `string` | The value passed in by users to the physical name prop of the resource. |
| [`region`](#cdkamazonchimeresourcesphoneassociationpropspropertyregion) | `string` | The AWS region this resource belongs to. |
| [`e164PhoneNumber`](#cdkamazonchimeresourcesphoneassociationpropspropertye164phonenumber)<span title="Required">*</span> | `string` | *No description.* |
| [`voiceConnectorId`](#cdkamazonchimeresourcesphoneassociationpropspropertyvoiceconnectorid)<span title="Required">*</span> | `string` | *No description.* |

---

##### `account`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.account" id="cdkamazonchimeresourcesphoneassociationpropspropertyaccount"></a>

```typescript
public readonly account: string;
```

- *Type:* `string`
- *Default:* the resource is in the same account as the stack it belongs to

The AWS account ID this resource belongs to.

---

##### `environmentFromArn`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.environmentFromArn" id="cdkamazonchimeresourcesphoneassociationpropspropertyenvironmentfromarn"></a>

```typescript
public readonly environmentFromArn: string;
```

- *Type:* `string`
- *Default:* take environment from `account`, `region` parameters, or use Stack environment.

ARN to deduce region and account from.

The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources.  Cannot be supplied together with either `account` or `region`.

---

##### `physicalName`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.physicalName" id="cdkamazonchimeresourcesphoneassociationpropspropertyphysicalname"></a>

```typescript
public readonly physicalName: string;
```

- *Type:* `string`
- *Default:* The physical name will be allocated by CloudFormation at deployment time

The value passed in by users to the physical name prop of the resource.

`undefined` implies that a physical name will be allocated by    CloudFormation during deployment. - a concrete value implies a specific physical name - `PhysicalName.GENERATE_IF_NEEDED` is a marker that indicates that a physical will only be generated    by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

---

##### `region`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.region" id="cdkamazonchimeresourcesphoneassociationpropspropertyregion"></a>

```typescript
public readonly region: string;
```

- *Type:* `string`
- *Default:* the resource is in the same region as the stack it belongs to

The AWS region this resource belongs to.

---

##### `e164PhoneNumber`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.e164PhoneNumber" id="cdkamazonchimeresourcesphoneassociationpropspropertye164phonenumber"></a>

```typescript
public readonly e164PhoneNumber: string;
```

- *Type:* `string`

---

##### `voiceConnectorId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneAssociationProps.property.voiceConnectorId" id="cdkamazonchimeresourcesphoneassociationpropspropertyvoiceconnectorid"></a>

```typescript
public readonly voiceConnectorId: string;
```

- *Type:* `string`

---

### PhoneNumberProps <a name="cdk-amazon-chime-resources.PhoneNumberProps" id="cdkamazonchimeresourcesphonenumberprops"></a>

Props for `PhoneNumber`.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { PhoneNumberProps } from 'cdk-amazon-chime-resources'

const phoneNumberProps: PhoneNumberProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`phoneProductType`](#cdkamazonchimeresourcesphonenumberpropspropertyphoneproducttype)<span title="Required">*</span> | [`cdk-amazon-chime-resources.PhoneProductType`](#cdk-amazon-chime-resources.PhoneProductType) | Phone Product Type (required) - SipMediaApplicationDialIn or VoiceConnector. |
| [`phoneAreaCode`](#cdkamazonchimeresourcesphonenumberpropspropertyphoneareacode) | `number` | Area Code for phone number request (optional)  - Usable only with US Country. |
| [`phoneCity`](#cdkamazonchimeresourcesphonenumberpropspropertyphonecity) | `string` | City for phone number request (optional) - Usable only with US Country. |
| [`phoneCountry`](#cdkamazonchimeresourcesphonenumberpropspropertyphonecountry) | [`cdk-amazon-chime-resources.PhoneCountry`](#cdk-amazon-chime-resources.PhoneCountry) | Country for phone number request (optional) - See https://docs.aws.amazon.com/chime/latest/ag/phone-country-reqs.html for more details. |
| [`phoneNumberTollFreePrefix`](#cdkamazonchimeresourcesphonenumberpropspropertyphonenumbertollfreeprefix) | `number` | Toll Free Prefix for phone number request (optional). |
| [`phoneNumberType`](#cdkamazonchimeresourcesphonenumberpropspropertyphonenumbertype) | [`cdk-amazon-chime-resources.PhoneNumberType`](#cdk-amazon-chime-resources.PhoneNumberType) | Phone Number Type for phone number request (optional) - Local or TollFree - Required with non-US country. |
| [`phoneState`](#cdkamazonchimeresourcesphonenumberpropspropertyphonestate) | `string` | State for phone number request (optional) - Usable only with US Country. |

---

##### `phoneProductType`<sup>Required</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneProductType" id="cdkamazonchimeresourcesphonenumberpropspropertyphoneproducttype"></a>

```typescript
public readonly phoneProductType: PhoneProductType;
```

- *Type:* [`cdk-amazon-chime-resources.PhoneProductType`](#cdk-amazon-chime-resources.PhoneProductType)
- *Default:* None

Phone Product Type (required) - SipMediaApplicationDialIn or VoiceConnector.

---

##### `phoneAreaCode`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneAreaCode" id="cdkamazonchimeresourcesphonenumberpropspropertyphoneareacode"></a>

```typescript
public readonly phoneAreaCode: number;
```

- *Type:* `number`
- *Default:* None

Area Code for phone number request (optional)  - Usable only with US Country.

---

##### `phoneCity`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneCity" id="cdkamazonchimeresourcesphonenumberpropspropertyphonecity"></a>

```typescript
public readonly phoneCity: string;
```

- *Type:* `string`
- *Default:* None

City for phone number request (optional) - Usable only with US Country.

---

##### `phoneCountry`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneCountry" id="cdkamazonchimeresourcesphonenumberpropspropertyphonecountry"></a>

```typescript
public readonly phoneCountry: PhoneCountry;
```

- *Type:* [`cdk-amazon-chime-resources.PhoneCountry`](#cdk-amazon-chime-resources.PhoneCountry)
- *Default:* US

Country for phone number request (optional) - See https://docs.aws.amazon.com/chime/latest/ag/phone-country-reqs.html for more details.

---

##### `phoneNumberTollFreePrefix`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneNumberTollFreePrefix" id="cdkamazonchimeresourcesphonenumberpropspropertyphonenumbertollfreeprefix"></a>

```typescript
public readonly phoneNumberTollFreePrefix: number;
```

- *Type:* `number`
- *Default:* None

Toll Free Prefix for phone number request (optional).

---

##### `phoneNumberType`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneNumberType" id="cdkamazonchimeresourcesphonenumberpropspropertyphonenumbertype"></a>

```typescript
public readonly phoneNumberType: PhoneNumberType;
```

- *Type:* [`cdk-amazon-chime-resources.PhoneNumberType`](#cdk-amazon-chime-resources.PhoneNumberType)
- *Default:* None

Phone Number Type for phone number request (optional) - Local or TollFree - Required with non-US country.

---

##### `phoneState`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.PhoneNumberProps.property.phoneState" id="cdkamazonchimeresourcesphonenumberpropspropertyphonestate"></a>

```typescript
public readonly phoneState: string;
```

- *Type:* `string`
- *Default:* None

State for phone number request (optional) - Usable only with US Country.

---

### Routes <a name="cdk-amazon-chime-resources.Routes" id="cdkamazonchimeresourcesroutes"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { Routes } from 'cdk-amazon-chime-resources'

const routes: Routes = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`host`](#cdkamazonchimeresourcesroutespropertyhost)<span title="Required">*</span> | `string` | *No description.* |
| [`port`](#cdkamazonchimeresourcesroutespropertyport)<span title="Required">*</span> | `number` | *No description.* |
| [`priority`](#cdkamazonchimeresourcesroutespropertypriority)<span title="Required">*</span> | `number` | *No description.* |
| [`protocol`](#cdkamazonchimeresourcesroutespropertyprotocol)<span title="Required">*</span> | [`cdk-amazon-chime-resources.Protocol`](#cdk-amazon-chime-resources.Protocol) | *No description.* |
| [`weight`](#cdkamazonchimeresourcesroutespropertyweight)<span title="Required">*</span> | `number` | *No description.* |

---

##### `host`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Routes.property.host" id="cdkamazonchimeresourcesroutespropertyhost"></a>

```typescript
public readonly host: string;
```

- *Type:* `string`

---

##### `port`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Routes.property.port" id="cdkamazonchimeresourcesroutespropertyport"></a>

```typescript
public readonly port: number;
```

- *Type:* `number`

---

##### `priority`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Routes.property.priority" id="cdkamazonchimeresourcesroutespropertypriority"></a>

```typescript
public readonly priority: number;
```

- *Type:* `number`

---

##### `protocol`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Routes.property.protocol" id="cdkamazonchimeresourcesroutespropertyprotocol"></a>

```typescript
public readonly protocol: Protocol;
```

- *Type:* [`cdk-amazon-chime-resources.Protocol`](#cdk-amazon-chime-resources.Protocol)

---

##### `weight`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Routes.property.weight" id="cdkamazonchimeresourcesroutespropertyweight"></a>

```typescript
public readonly weight: number;
```

- *Type:* `number`

---

### SipMediaAppProps <a name="cdk-amazon-chime-resources.SipMediaAppProps" id="cdkamazonchimeresourcessipmediaappprops"></a>

Props for `SipMediaApplication`.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { SipMediaAppProps } from 'cdk-amazon-chime-resources'

const sipMediaAppProps: SipMediaAppProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`endpoint`](#cdkamazonchimeresourcessipmediaapppropspropertyendpoint)<span title="Required">*</span> | `string` | endpoint for SipMediaApplication(required). |
| [`name`](#cdkamazonchimeresourcessipmediaapppropspropertyname) | `string` | name for SipMediaApplication (optional). |
| [`region`](#cdkamazonchimeresourcessipmediaapppropspropertyregion) | `string` | region for SipMediaApplication(required) - Must us-east-1 or us-west-2 and in the same region as the SipMediaApplication Lambda handler. |

---

##### `endpoint`<sup>Required</sup> <a name="cdk-amazon-chime-resources.SipMediaAppProps.property.endpoint" id="cdkamazonchimeresourcessipmediaapppropspropertyendpoint"></a>

```typescript
public readonly endpoint: string;
```

- *Type:* `string`
- *Default:* none

endpoint for SipMediaApplication(required).

---

##### `name`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.SipMediaAppProps.property.name" id="cdkamazonchimeresourcessipmediaapppropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`
- *Default:* unique ID for resource

name for SipMediaApplication (optional).

---

##### `region`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.SipMediaAppProps.property.region" id="cdkamazonchimeresourcessipmediaapppropspropertyregion"></a>

```typescript
public readonly region: string;
```

- *Type:* `string`
- *Default:* same region as stack deployment

region for SipMediaApplication(required) - Must us-east-1 or us-west-2 and in the same region as the SipMediaApplication Lambda handler.

---

### SipRuleProps <a name="cdk-amazon-chime-resources.SipRuleProps" id="cdkamazonchimeresourcessipruleprops"></a>

Props for `SipRule`.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { SipRuleProps } from 'cdk-amazon-chime-resources'

const sipRuleProps: SipRuleProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`targetApplications`](#cdkamazonchimeresourcessiprulepropspropertytargetapplications)<span title="Required">*</span> | [`cdk-amazon-chime-resources.TargetApplications`](#cdk-amazon-chime-resources.TargetApplications)[] | *No description.* |
| [`triggerType`](#cdkamazonchimeresourcessiprulepropspropertytriggertype)<span title="Required">*</span> | [`cdk-amazon-chime-resources.TriggerType`](#cdk-amazon-chime-resources.TriggerType) | Trigger Type for SipRule (required) - TO_PHONE_NUMBER or REQUEST_URI_HOSTNAME. |
| [`triggerValue`](#cdkamazonchimeresourcessiprulepropspropertytriggervalue)<span title="Required">*</span> | `string` | Trigger Value for SipRule (required) - EE.164 Phone Number or Voice Connector URI. |
| [`name`](#cdkamazonchimeresourcessiprulepropspropertyname) | `string` | name for SipRule (optional). |

---

##### `targetApplications`<sup>Required</sup> <a name="cdk-amazon-chime-resources.SipRuleProps.property.targetApplications" id="cdkamazonchimeresourcessiprulepropspropertytargetapplications"></a>

```typescript
public readonly targetApplications: TargetApplications[];
```

- *Type:* [`cdk-amazon-chime-resources.TargetApplications`](#cdk-amazon-chime-resources.TargetApplications)[]

---

##### `triggerType`<sup>Required</sup> <a name="cdk-amazon-chime-resources.SipRuleProps.property.triggerType" id="cdkamazonchimeresourcessiprulepropspropertytriggertype"></a>

```typescript
public readonly triggerType: TriggerType;
```

- *Type:* [`cdk-amazon-chime-resources.TriggerType`](#cdk-amazon-chime-resources.TriggerType)
- *Default:* none

Trigger Type for SipRule (required) - TO_PHONE_NUMBER or REQUEST_URI_HOSTNAME.

---

##### `triggerValue`<sup>Required</sup> <a name="cdk-amazon-chime-resources.SipRuleProps.property.triggerValue" id="cdkamazonchimeresourcessiprulepropspropertytriggervalue"></a>

```typescript
public readonly triggerValue: string;
```

- *Type:* `string`
- *Default:* none

Trigger Value for SipRule (required) - EE.164 Phone Number or Voice Connector URI.

---

##### `name`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.SipRuleProps.property.name" id="cdkamazonchimeresourcessiprulepropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`
- *Default:* unique ID for resource

name for SipRule (optional).

---

### Streaming <a name="cdk-amazon-chime-resources.Streaming" id="cdkamazonchimeresourcesstreaming"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { Streaming } from 'cdk-amazon-chime-resources'

const streaming: Streaming = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`dataRetention`](#cdkamazonchimeresourcesstreamingpropertydataretention)<span title="Required">*</span> | `number` | Streaming data retention for VoiceConnector. |
| [`enabled`](#cdkamazonchimeresourcesstreamingpropertyenabled)<span title="Required">*</span> | `boolean` | *No description.* |
| [`notificationTargets`](#cdkamazonchimeresourcesstreamingpropertynotificationtargets)<span title="Required">*</span> | [`cdk-amazon-chime-resources.NotificationTargetType`](#cdk-amazon-chime-resources.NotificationTargetType)[] | Streaming data retention for VoiceConnector. |

---

##### `dataRetention`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Streaming.property.dataRetention" id="cdkamazonchimeresourcesstreamingpropertydataretention"></a>

```typescript
public readonly dataRetention: number;
```

- *Type:* `number`
- *Default:* 0

Streaming data retention for VoiceConnector.

---

##### `enabled`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Streaming.property.enabled" id="cdkamazonchimeresourcesstreamingpropertyenabled"></a>

```typescript
public readonly enabled: boolean;
```

- *Type:* `boolean`

---

##### `notificationTargets`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Streaming.property.notificationTargets" id="cdkamazonchimeresourcesstreamingpropertynotificationtargets"></a>

```typescript
public readonly notificationTargets: NotificationTargetType[];
```

- *Type:* [`cdk-amazon-chime-resources.NotificationTargetType`](#cdk-amazon-chime-resources.NotificationTargetType)[]
- *Default:* 0

Streaming data retention for VoiceConnector.

---

### TargetApplications <a name="cdk-amazon-chime-resources.TargetApplications" id="cdkamazonchimeresourcestargetapplications"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { TargetApplications } from 'cdk-amazon-chime-resources'

const targetApplications: TargetApplications = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`priority`](#cdkamazonchimeresourcestargetapplicationspropertypriority)<span title="Required">*</span> | `number` | Priority for SipRule (required) - 1 to 25. |
| [`sipMediaApplicationId`](#cdkamazonchimeresourcestargetapplicationspropertysipmediaapplicationid)<span title="Required">*</span> | `string` | SipMediaApplicationId for SipRule (required). |
| [`region`](#cdkamazonchimeresourcestargetapplicationspropertyregion) | `string` | Region for SipRule (optional). |

---

##### `priority`<sup>Required</sup> <a name="cdk-amazon-chime-resources.TargetApplications.property.priority" id="cdkamazonchimeresourcestargetapplicationspropertypriority"></a>

```typescript
public readonly priority: number;
```

- *Type:* `number`
- *Default:* none

Priority for SipRule (required) - 1 to 25.

---

##### `sipMediaApplicationId`<sup>Required</sup> <a name="cdk-amazon-chime-resources.TargetApplications.property.sipMediaApplicationId" id="cdkamazonchimeresourcestargetapplicationspropertysipmediaapplicationid"></a>

```typescript
public readonly sipMediaApplicationId: string;
```

- *Type:* `string`
- *Default:* none

SipMediaApplicationId for SipRule (required).

---

##### `region`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.TargetApplications.property.region" id="cdkamazonchimeresourcestargetapplicationspropertyregion"></a>

```typescript
public readonly region: string;
```

- *Type:* `string`
- *Default:* same region as stack deployment

Region for SipRule (optional).

---

### Termination <a name="cdk-amazon-chime-resources.Termination" id="cdkamazonchimeresourcestermination"></a>

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { Termination } from 'cdk-amazon-chime-resources'

const termination: Termination = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`callingRegions`](#cdkamazonchimeresourcesterminationpropertycallingregions)<span title="Required">*</span> | `string`[] | Calling Regions for VoiceConnector (optional). |
| [`terminationCidrs`](#cdkamazonchimeresourcesterminationpropertyterminationcidrs)<span title="Required">*</span> | `string`[] | termination IP for VoiceConnector (optional). |

---

##### `callingRegions`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Termination.property.callingRegions" id="cdkamazonchimeresourcesterminationpropertycallingregions"></a>

```typescript
public readonly callingRegions: string[];
```

- *Type:* `string`[]
- *Default:* ['US']

Calling Regions for VoiceConnector (optional).

---

##### `terminationCidrs`<sup>Required</sup> <a name="cdk-amazon-chime-resources.Termination.property.terminationCidrs" id="cdkamazonchimeresourcesterminationpropertyterminationcidrs"></a>

```typescript
public readonly terminationCidrs: string[];
```

- *Type:* `string`[]
- *Default:* none

termination IP for VoiceConnector (optional).

---

### VoiceConnectorProps <a name="cdk-amazon-chime-resources.VoiceConnectorProps" id="cdkamazonchimeresourcesvoiceconnectorprops"></a>

Props for `SipMediaApplication`.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { VoiceConnectorProps } from 'cdk-amazon-chime-resources'

const voiceConnectorProps: VoiceConnectorProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`encryption`](#cdkamazonchimeresourcesvoiceconnectorpropspropertyencryption) | `boolean` | Encryption boolean for VoiceConnector. |
| [`logging`](#cdkamazonchimeresourcesvoiceconnectorpropspropertylogging) | [`cdk-amazon-chime-resources.Logging`](#cdk-amazon-chime-resources.Logging) | *No description.* |
| [`name`](#cdkamazonchimeresourcesvoiceconnectorpropspropertyname) | `string` | name for VoiceConnector. |
| [`origination`](#cdkamazonchimeresourcesvoiceconnectorpropspropertyorigination) | [`cdk-amazon-chime-resources.Routes`](#cdk-amazon-chime-resources.Routes)[] | *No description.* |
| [`region`](#cdkamazonchimeresourcesvoiceconnectorpropspropertyregion) | `string` | region for SipMediaApplication(required) - Must us-east-1 or us-west-2 and in the same region as the SipMediaApplication Lambda handler. |
| [`streaming`](#cdkamazonchimeresourcesvoiceconnectorpropspropertystreaming) | [`cdk-amazon-chime-resources.Streaming`](#cdk-amazon-chime-resources.Streaming) | *No description.* |
| [`termination`](#cdkamazonchimeresourcesvoiceconnectorpropspropertytermination) | [`cdk-amazon-chime-resources.Termination`](#cdk-amazon-chime-resources.Termination) | *No description.* |

---

##### `encryption`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.encryption" id="cdkamazonchimeresourcesvoiceconnectorpropspropertyencryption"></a>

```typescript
public readonly encryption: boolean;
```

- *Type:* `boolean`
- *Default:* False

Encryption boolean for VoiceConnector.

---

##### `logging`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.logging" id="cdkamazonchimeresourcesvoiceconnectorpropspropertylogging"></a>

```typescript
public readonly logging: Logging;
```

- *Type:* [`cdk-amazon-chime-resources.Logging`](#cdk-amazon-chime-resources.Logging)

---

##### `name`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.name" id="cdkamazonchimeresourcesvoiceconnectorpropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`
- *Default:* unique ID for resource

name for VoiceConnector.

---

##### `origination`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.origination" id="cdkamazonchimeresourcesvoiceconnectorpropspropertyorigination"></a>

```typescript
public readonly origination: Routes[];
```

- *Type:* [`cdk-amazon-chime-resources.Routes`](#cdk-amazon-chime-resources.Routes)[]

---

##### `region`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.region" id="cdkamazonchimeresourcesvoiceconnectorpropspropertyregion"></a>

```typescript
public readonly region: string;
```

- *Type:* `string`
- *Default:* same region as stack deployment

region for SipMediaApplication(required) - Must us-east-1 or us-west-2 and in the same region as the SipMediaApplication Lambda handler.

---

##### `streaming`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.streaming" id="cdkamazonchimeresourcesvoiceconnectorpropspropertystreaming"></a>

```typescript
public readonly streaming: Streaming;
```

- *Type:* [`cdk-amazon-chime-resources.Streaming`](#cdk-amazon-chime-resources.Streaming)

---

##### `termination`<sup>Optional</sup> <a name="cdk-amazon-chime-resources.VoiceConnectorProps.property.termination" id="cdkamazonchimeresourcesvoiceconnectorpropspropertytermination"></a>

```typescript
public readonly termination: Termination;
```

- *Type:* [`cdk-amazon-chime-resources.Termination`](#cdk-amazon-chime-resources.Termination)

---



## Enums <a name="Enums" id="enums"></a>

### NotificationTargetType <a name="NotificationTargetType" id="notificationtargettype"></a>

| **Name** | **Description** |
| --- | --- |
| [`EVENTBRIDGE`](#cdkamazonchimeresourcesnotificationtargettypeeventbridge) | *No description.* |
| [`SNS`](#cdkamazonchimeresourcesnotificationtargettypesns) | *No description.* |
| [`SQS`](#cdkamazonchimeresourcesnotificationtargettypesqs) | *No description.* |

---

#### `EVENTBRIDGE` <a name="cdk-amazon-chime-resources.NotificationTargetType.EVENTBRIDGE" id="cdkamazonchimeresourcesnotificationtargettypeeventbridge"></a>

---


#### `SNS` <a name="cdk-amazon-chime-resources.NotificationTargetType.SNS" id="cdkamazonchimeresourcesnotificationtargettypesns"></a>

---


#### `SQS` <a name="cdk-amazon-chime-resources.NotificationTargetType.SQS" id="cdkamazonchimeresourcesnotificationtargettypesqs"></a>

---


### PhoneCountry <a name="PhoneCountry" id="phonecountry"></a>

| **Name** | **Description** |
| --- | --- |
| [`AU`](#cdkamazonchimeresourcesphonecountryau) | *No description.* |
| [`AT`](#cdkamazonchimeresourcesphonecountryat) | *No description.* |
| [`CA`](#cdkamazonchimeresourcesphonecountryca) | *No description.* |
| [`DK`](#cdkamazonchimeresourcesphonecountrydk) | *No description.* |
| [`DE`](#cdkamazonchimeresourcesphonecountryde) | *No description.* |
| [`IE`](#cdkamazonchimeresourcesphonecountryie) | *No description.* |
| [`IT`](#cdkamazonchimeresourcesphonecountryit) | *No description.* |
| [`NZ`](#cdkamazonchimeresourcesphonecountrynz) | *No description.* |
| [`NG`](#cdkamazonchimeresourcesphonecountryng) | *No description.* |
| [`PR`](#cdkamazonchimeresourcesphonecountrypr) | *No description.* |
| [`KR`](#cdkamazonchimeresourcesphonecountrykr) | *No description.* |
| [`SE`](#cdkamazonchimeresourcesphonecountryse) | *No description.* |
| [`CH`](#cdkamazonchimeresourcesphonecountrych) | *No description.* |
| [`UK`](#cdkamazonchimeresourcesphonecountryuk) | *No description.* |
| [`US`](#cdkamazonchimeresourcesphonecountryus) | *No description.* |

---

#### `AU` <a name="cdk-amazon-chime-resources.PhoneCountry.AU" id="cdkamazonchimeresourcesphonecountryau"></a>

---


#### `AT` <a name="cdk-amazon-chime-resources.PhoneCountry.AT" id="cdkamazonchimeresourcesphonecountryat"></a>

---


#### `CA` <a name="cdk-amazon-chime-resources.PhoneCountry.CA" id="cdkamazonchimeresourcesphonecountryca"></a>

---


#### `DK` <a name="cdk-amazon-chime-resources.PhoneCountry.DK" id="cdkamazonchimeresourcesphonecountrydk"></a>

---


#### `DE` <a name="cdk-amazon-chime-resources.PhoneCountry.DE" id="cdkamazonchimeresourcesphonecountryde"></a>

---


#### `IE` <a name="cdk-amazon-chime-resources.PhoneCountry.IE" id="cdkamazonchimeresourcesphonecountryie"></a>

---


#### `IT` <a name="cdk-amazon-chime-resources.PhoneCountry.IT" id="cdkamazonchimeresourcesphonecountryit"></a>

---


#### `NZ` <a name="cdk-amazon-chime-resources.PhoneCountry.NZ" id="cdkamazonchimeresourcesphonecountrynz"></a>

---


#### `NG` <a name="cdk-amazon-chime-resources.PhoneCountry.NG" id="cdkamazonchimeresourcesphonecountryng"></a>

---


#### `PR` <a name="cdk-amazon-chime-resources.PhoneCountry.PR" id="cdkamazonchimeresourcesphonecountrypr"></a>

---


#### `KR` <a name="cdk-amazon-chime-resources.PhoneCountry.KR" id="cdkamazonchimeresourcesphonecountrykr"></a>

---


#### `SE` <a name="cdk-amazon-chime-resources.PhoneCountry.SE" id="cdkamazonchimeresourcesphonecountryse"></a>

---


#### `CH` <a name="cdk-amazon-chime-resources.PhoneCountry.CH" id="cdkamazonchimeresourcesphonecountrych"></a>

---


#### `UK` <a name="cdk-amazon-chime-resources.PhoneCountry.UK" id="cdkamazonchimeresourcesphonecountryuk"></a>

---


#### `US` <a name="cdk-amazon-chime-resources.PhoneCountry.US" id="cdkamazonchimeresourcesphonecountryus"></a>

---


### PhoneNumberType <a name="PhoneNumberType" id="phonenumbertype"></a>

| **Name** | **Description** |
| --- | --- |
| [`LOCAL`](#cdkamazonchimeresourcesphonenumbertypelocal) | *No description.* |
| [`TOLLFREE`](#cdkamazonchimeresourcesphonenumbertypetollfree) | *No description.* |

---

#### `LOCAL` <a name="cdk-amazon-chime-resources.PhoneNumberType.LOCAL" id="cdkamazonchimeresourcesphonenumbertypelocal"></a>

---


#### `TOLLFREE` <a name="cdk-amazon-chime-resources.PhoneNumberType.TOLLFREE" id="cdkamazonchimeresourcesphonenumbertypetollfree"></a>

---


### PhoneProductType <a name="PhoneProductType" id="phoneproducttype"></a>

| **Name** | **Description** |
| --- | --- |
| [`SMA`](#cdkamazonchimeresourcesphoneproducttypesma) | *No description.* |
| [`VC`](#cdkamazonchimeresourcesphoneproducttypevc) | *No description.* |

---

#### `SMA` <a name="cdk-amazon-chime-resources.PhoneProductType.SMA" id="cdkamazonchimeresourcesphoneproducttypesma"></a>

---


#### `VC` <a name="cdk-amazon-chime-resources.PhoneProductType.VC" id="cdkamazonchimeresourcesphoneproducttypevc"></a>

---


### Protocol <a name="Protocol" id="protocol"></a>

| **Name** | **Description** |
| --- | --- |
| [`TCP`](#cdkamazonchimeresourcesprotocoltcp) | *No description.* |
| [`UDP`](#cdkamazonchimeresourcesprotocoludp) | *No description.* |

---

#### `TCP` <a name="cdk-amazon-chime-resources.Protocol.TCP" id="cdkamazonchimeresourcesprotocoltcp"></a>

---


#### `UDP` <a name="cdk-amazon-chime-resources.Protocol.UDP" id="cdkamazonchimeresourcesprotocoludp"></a>

---


### TriggerType <a name="TriggerType" id="triggertype"></a>

| **Name** | **Description** |
| --- | --- |
| [`TO_PHONE_NUMBER`](#cdkamazonchimeresourcestriggertypetophonenumber) | *No description.* |
| [`REQUEST_URI_HOSTNAME`](#cdkamazonchimeresourcestriggertyperequesturihostname) | *No description.* |

---

#### `TO_PHONE_NUMBER` <a name="cdk-amazon-chime-resources.TriggerType.TO_PHONE_NUMBER" id="cdkamazonchimeresourcestriggertypetophonenumber"></a>

---


#### `REQUEST_URI_HOSTNAME` <a name="cdk-amazon-chime-resources.TriggerType.REQUEST_URI_HOSTNAME" id="cdkamazonchimeresourcestriggertyperequesturihostname"></a>

---

