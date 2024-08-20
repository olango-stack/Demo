export const handler = async(
    event, context
) => {
    console.log('Event', event);

    const x = event.x;
    const y = event.y;

    return x*y;
};


