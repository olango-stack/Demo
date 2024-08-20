exports.handler = async (event) => {
    const x = event.x;
    const y = event.y;

    const result = x * y;

    console.log('Multiplication result: ${result}');

    return {
        statusCode: 200,
        body: JSON.stringify(result)
    };
};

//Javascript allows a method to be called with more arguments than are actually defined