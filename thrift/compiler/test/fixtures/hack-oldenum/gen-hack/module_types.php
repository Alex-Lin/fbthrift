<?hh
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

namespace test\fixtures\oldenum;

/**
 * Original thrift enum:-
 * MyEnum
 */
newtype \test\fixtures\oldenum\MyEnumType = int;
final class \test\fixtures\oldenum\MyEnum extends Enum<\test\fixtures\oldenum\MyEnumType> {
  const \test\fixtures\oldenum\MyEnumType   MyValue1 = 0;
  const \test\fixtures\oldenum\MyEnumType   MyValue2 = 1;
  public static array $__names = array(
    0 => 'MyValue1',
    1 => 'MyValue2',
  );
  public static array $__values = array(
    'MyValue1' => 0,
    'MyValue2' => 1,
  );
}

