<link rel="stylesheet" type='text/css' href='main.css' />
<link rel="stylesheet" type='text/css' href='query.css' />
<link rel="stylesheet" type='text/css' href='bootstrap.css' />
<script src='jquery-1.9.0.min.js'></script>
<script src='query.js'></script>

<div class='wrapper'>

    <div class='logo'>
        <img src='logo.png'></img>
    </div>

    <div id='search-form'>
        <form method='POST' action='/query'>
            <input class='input-large' placeholder='Enter Slogan here...' name="value" type="text-area" />
            <input class='submit-button btn' type="submit" text="solve" />
        </form>
    </div>

    <div class='table-wrapper hide'>
    %if values:
        <div class='output'>
            <table class='table table-bordered'>
                <caption>Your problem has been solved!</caption>
                <thead>
                    <th></th>
                    <th>Field</th>
                    <th>Value</th>
                </thead>
                <tbody>
                    %for value in values:
                        <tr class='row'>
                            <td>
                                {{value}}
                            </td>
                            <td>
                                {{values[value]}}
                            </td>
                        </tr>
                    %end
            </table>
        </div>
    %end
    </div>
</div>

